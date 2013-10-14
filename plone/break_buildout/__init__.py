# -*- coding: utf-8 -*-


from plone.break_core import VulnerabilityCheck as VC
from plone.break_core import SecurityError
from zc.buildout import UserError

import logging
import pkg_resources

disclaimer = \
"""If you have a good reason to bypass this restriction,
remove the plone.break_buildout extension from your buildout."""


def check_vulnerability(buildout, logger):
    """ Refuse to run if a unsecure Plone setup is tried to be installed """

    plone_version = buildout['versions'].('Plone', '0.0.0')

    vc = VC(plone_version)

    if not vc.isSecure():
        logger.error("""
You try to build a Plone Instance that is not secure.
You have Plone {0} installed, for this version apply following patches:
 * {1}
    		""".format(plone_version, "\n * ".join(vc.getPatches())))
        raise SecurityError('User attemped to build an insecure Plone instance.')


def main(buildout):
    logger = logging.getLogger("plone.break_buildout")
    check_vulnerability(buildout, logger)
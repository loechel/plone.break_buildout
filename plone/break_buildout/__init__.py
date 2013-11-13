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
    extensions = buildout.get('buildout', {}).get('extensions',[]).split('\n')

    if (not buildout.offline) or ('buildout.autoapplyplonehotfixes' in extensions):
        plone_version = buildout.get('versions', {}).get('plone', '0.0.0')

        vc = VC(plone_version)
        #import ipdb; ipdb.set_trace()

        if not vc.isSecure():
            logger.error("""
You try to build a Plone Instance that is not secure.
You have Plone %s installed, for this version apply following patches:%s
        		""", plone_version, "\n * ".join(vc.getPatches()))
            raise SecurityError('User attemped to build an insecure Plone instance.')


def main(buildout):
    logger = logging.getLogger("plone.break_buildout")
    check_vulnerability(buildout, logger)
#!/usr/bin/env python3

'''
It displays all versions of module
'''

__author__ = 'Bartłomiej "furas" Burek'

import sys
from pip.basecommand import Command
from pip.index import PackageFinder

class AllVersionsCommand(Command):

    name = 'all_versions'

    def run(self, package_name):

        # PackageFinder requires session which requires options

        options, args = self.parse_args([])
        session = self._build_session(options=options)
        
        finder = PackageFinder(
            find_links=[],
            index_urls=["https://pypi.python.org/simple/"],
            session=session,
        )
       
        candidates = finder.find_all_candidates(package_name)
        
        # set() to remove repeated versions - ie. matplotlib
        versions = sorted(set(c.version for c in candidates))
        
        print('\n'.join(map(str, versions)))
 
if __name__ == '__main__': 
    AllVersionsCommand().run(sys.argv[1])

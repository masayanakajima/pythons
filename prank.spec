# -*- mode: python -*-
a = Analysis(['prank.py'],
             pathex=['C:\\Python'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='prank.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )

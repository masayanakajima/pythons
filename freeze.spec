# -*- mode: python -*-
a = Analysis(['freeze.py'],
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
          name='freeze.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )

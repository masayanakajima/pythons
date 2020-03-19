# -*- mode: python -*-
a = Analysis(['next.py', 'BroadcastObserver.py'],
             pathex=['C:\\Python\\next'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='next.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )

# -*- mode: python -*-
a = Analysis(['chat.py', 'ip.txt'],
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
          name='chat.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

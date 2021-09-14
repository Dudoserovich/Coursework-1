# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['.\\venv\\', 'C:\\Windows\\WinSxS\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.19041.1_none_21374cb0681a6320', 'C:\\MyPrograms\\Kursach'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )

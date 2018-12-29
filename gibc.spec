# -*- mode: python -*-

block_cipher = None


a = Analysis(['gibc'],
             pathex=['/home/henrik/Programming/backup_client'],
             binaries=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gibc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

import shutil
shutil.copyfile('default_config', 'dist/default_config')
shutil.copyfile('icon.png', 'dist/icon.png')

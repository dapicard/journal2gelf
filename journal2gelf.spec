# -*- mode: python -*-
a = Analysis(['journal2gelf'],
             pathex=['/home/sam/gcloud/graylog/journal2gelf'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='journal2gelf',
          debug=False,
          strip=None,
          upx=True,
          console=True )

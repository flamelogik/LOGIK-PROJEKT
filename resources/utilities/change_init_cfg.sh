cd /opt/Autodesk/.flamefamily_2025.1.1/cfg/

sudo tar -czpf init.cfg.bak_$(date +%m%d%Y_%H%M).tgz init.cfg

For MacOS: sudo sed -i '' -E 's/(DTVsync|601sync)$/freesync/g' init.cfg
For Rocky: sudo sed -i -E 's/(DTVsync|601sync)$/freesync/g' init.cfg

sudo sed -i -E 's/, aja, 1$/, NDI, 1/g' init.cfg
, aja, 
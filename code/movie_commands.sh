ffmpeg -i png/frame%04d.png -filter:v 'setpts=0.1*PTS' -vb 8000K hp35_msm.mpg
ffmpeg -i png/frame%04d.png -filter:v 'setpts=0.1*PTS' -vb 8000K hp35_msm.mp4
theora_png2theora png/frame%04d.png -o hp35_msm.ogv -v 5 -f 10000 -F 40
theora_png2theora png/frame%04d.png -o hp35_msm_lossy.ogv -v 2 -f 10000 -F 40

hide lines, name 1HB+1HD+1HE+1HG+2HB+2HD+2HE+2HG+3HE+H+H2+H3+HA+HA2+HA3+HB+HB1+HB2+HB3+HD1+HD11+HD12+HD13+HD2+HD21+HD22+HD23+HD3+HE+HE1+HE2+HE21+HE22+HE3+HG+HG1+HG11+HG12+HG13+HG2+HG21+HG22+HG23+HG3+HH11+HH12+HH2+HH21+HH22+HZ+HZ1+HZ2+HZ3+1HD1+1HD2+3HD1+3HD2+2HD2+1HD2+2HD1+1HH1+1HH2+2HH1+2HH2+1HZ+2HZ+3HZ+1H+2H+3H+1HG1+1HG2+1HG3+2HG1+2HG2+2HG3+3HG1+3HG2+3HG3+1HE1+1HE2+2HE1+2HE2+1HA+2HA

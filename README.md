## Installation on Windows using Anaconda
```
conda create -n MoviePy_Concatenate_Videoclips -y && conda activate MoviePy_Concatenate_Videoclips && conda install python=3.9.7 -y
git clone https://github.com/alex1779/MoviePy_Concatenate_Videoclips.git
cd MoviePy_Concatenate_Videoclips
pip install -r requirements.txt
```

## For running
```
python main.py -i input/ -o output/test.mp4
```

![Face Mesh](https://github.com/alex1779/MoviePy_Concatenate_Videoclips/blob/master/img.jpg)

## How Works

```
The -i parameter is the input path folder that must contains the video parts to merge, for example -i input/
The parameter -o is the path for the output file, for example -o output/test.mp4

Clarification:
1. All files inside the input folder will be added to the final file.
The files in the input folder must be exclusively in video format, e.g. .mp4, .avi ,.mpg and so on.

2. In the output path, in addition to the name, the final video format must be specified, e.g., .mp4, .avi, .mpg, and so on.


```

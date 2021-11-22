clc
clear all
close all

filenames = dir('test\*.png');
count = 1;
for j=1:length(filenames)
    img_png = imread(strcat('test\',filenames(j).name));
    [folder, fileName, extension] = fileparts(filenames(j).name);
    imwrite(img_png,strcat(fileName,'.jpg'),'Quality',100);
    count = count +1;
end
count

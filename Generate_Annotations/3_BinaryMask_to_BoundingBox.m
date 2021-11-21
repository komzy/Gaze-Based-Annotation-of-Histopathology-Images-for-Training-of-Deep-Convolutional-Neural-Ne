clear all
close all
clc
filenames = dir('*.png');
count = 1;
rows_out = {};
 %file = fopen('bbox_files2.txt', 'w');
for j=1:length(filenames)
    img_bw = imread(filenames(j).name);
    img_bw = im2bw(img_bw,0.5);
    % img_bw = imbinarize(img_bw);
    [height, width] = size(img_bw);
    %img_bw = imbinarize(img, 0);
    bb = regionprops(img_bw, 'BoundingBox');
    
    imshow(img_bw)
    hold on
    filenames(j).name
    length(bb)
    
    for i=1:length(bb)
        bbox =  ceil(bb(i).BoundingBox);
        rectangle('Position', [bbox(1),bbox(2),bbox(3),bbox(4)],'EdgeColor','r','LineWidth',2) ;
        rows{count} = {filenames(j).name; width; height; 'Keratin_Pearl'; num2str(bbox(1)-1); ...
            num2str(bbox(2)-1); num2str(bbox(1) -1 + bbox(3)); ...
            num2str(bbox(2) + bbox(4)-1)};
        rows_new = rows{count}';
        rows_out = [rows_out; rows_new];
        
        count = count + 1;
    end
    
    prompt = 'Continue?';
    xx = input(prompt)
    hold off
%    if length(bb) ~= 0
%         fprintf(j, strcat(filenames(j).name, '\n'));
%     end
end
%csvwrite('mitosis_labels.csv', cell2mat(rows))
%writetable(T,'myData.csv','Delimiter',',')
T = cell2table(rows_out)
writetable(T, 'train.csv');
%out = cell2mat(rows_out)
%xlsxwrite('test3.xlsx', rows_out')

clear all
load('train.mat')

t = 0:0.002:6-0.002;

nums = randi(900,900,1);
%nums2 = randi(450,450,1);

classes = zeros(900,1);
classes(1:150,1) = 1;
classes(151:300,1) = 2;
classes(301:450,1) = 3;
classes(451:600,1) = 4;
classes(601:750,1) = 5;
classes(751:900,1) = 6;
classes = [nums,classes];
%class_test = [nums2,classes];

%data_ch1 = [cyl_ch1_full(1:75,:);hook_ch1_full(1:75,:);lat_ch1_full(1:75,:);palm_ch1_full(1:75,:);spher_ch1_full(1:75,:);tip_ch1_full(1:75,:)];
%data_ch2 = [cyl_ch2_full(1:75,:);hook_ch2_full(1:75,:);lat_ch2_full(1:75,:);palm_ch2_full(1:75,:);spher_ch2_full(1:75,:);tip_ch2_full(1:75,:)];

data_ch1 = [cyl_ch1_full;hook_ch1_full;lat_ch1_full;palm_ch1_full;spher_ch1_full;tip_ch1_full];
data_ch2 = [cyl_ch2_full;hook_ch2_full;lat_ch2_full;palm_ch2_full;spher_ch2_full;tip_ch2_full];

%test_ch1 = [cyl_ch1_full(76:end,:);hook_ch1_full(76:end,:);lat_ch1_full(76:end,:);palm_ch1_full(76:end,:);spher_ch1_full(76:end,:);tip_ch1_full(76:end,:)];
%test_ch2 = [cyl_ch2_full(76:end,:);hook_ch2_full(76:end,:);lat_ch2_full(76:end,:);palm_ch2_full(76:end,:);spher_ch2_full(76:end,:);tip_ch2_full(76:end,:)];

for i=1:900
    data_full(i,:) = average_elems(data_ch1(i,:),data_ch2(i,:));
end
%data_full = data_ch1+data_ch2;
%test_full = test_ch1+test_ch2;

data_full = [classes,data_full];
%test_full = [class_test,test_full];

data_full = sortrows(data_full,1);
%test_full = sortrows(test_full,1);

data_full = data_full(:,2:end);
%test_full = test_full(:,2:end);

csvwrite('data_full.txt',data_full)
%csvwrite('test_full.txt',test_full)

function vec = average_elems(vec1, vec2)
for i=1:length(vec1)
    vec(i) = mean([vec1(i),vec2(i)]);
end
end





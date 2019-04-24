load('train.mat')

%t = 0:0.002:6-0.002;
%plot(t,spher_ch2_full(1,:))
%axis([0 6 -5 5])

nums1 = randi(450,450,1);
nums2 = randi(450,450,1);

classes = zeros(450,1);
classes(1:90,1) = 1;
classes(91:180,1) = 2;
classes(181:270,1) = 3;
classes(271:360,1) = 4;
classes(361:450,1) = 5;
class_train = [nums1,classes];
class_test = [nums2,classes];


train_ch1 = [cyl_ch1_full(1:75,:);hook_ch1_full(1:75,:);lat_ch1_full(1:75,:);palm_ch1_full(1:75,:);spher_ch1_full(1:75,:);tip_ch1_full(1:75,:)];
train_ch2 = [cyl_ch2_full(1:75,:);hook_ch2_full(1:75,:);lat_ch2_full(1:75,:);palm_ch2_full(1:75,:);spher_ch2_full(1:75,:);tip_ch2_full(1:75,:)];

test_ch1 = [cyl_ch1_full(76:end,:);hook_ch1_full(76:end,:);lat_ch1_full(76:end,:);palm_ch1_full(76:end,:);spher_ch1_full(76:end,:);tip_ch1_full(76:end,:)];
test_ch2 = [cyl_ch2_full(76:end,:);hook_ch2_full(76:end,:);lat_ch2_full(76:end,:);palm_ch2_full(76:end,:);spher_ch2_full(76:end,:);tip_ch2_full(76:end,:)];

train_ch1 = [class_train,train_ch1];
train_ch2 = [class_train,train_ch2];

test_ch1 = [class_test,test_ch1];
test_ch2 = [class_test,test_ch2];

train_ch1 = sortrows(train_ch1,1);
train_ch2 = sortrows(train_ch2,1);

test_ch1 = sortrows(test_ch1,1);
test_ch2 = sortrows(test_ch2,1);

train_ch1 = train_ch1(:,2:end);
train_ch2 = train_ch2(:,2:end);

test_ch1 = test_ch1(:,2:end);
test_ch2 = test_ch2(:,2:end);


csvwrite('train_ch1.txt',train_ch1)
csvwrite('train_ch2.txt',train_ch2)
csvwrite('test_ch1.txt',test_ch1)
csvwrite('test_ch2.txt',test_ch2)


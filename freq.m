clear all
data_full = csvread('complete_features_ch1.txt');
data_full1 = csvread('complete_features_ch2.txt');
data_full = [data_full;data_full1];
feats_full = data_full(:,3001:end);
data_full = data_full(:,1:3000);

%test = csvread('test_full.txt');

fs = 500;
t_step = 1/fs;
t = 0:t_step:6-0.002;
len = size(data_full);
len = len(1);
N = 200;
for i=1:len
    X = fft(data_full(i,2:end),N);
    X = X(1:N/2); %restricts X to positive domain only
    X1 = abs(X); %magnitude
    X1 = X1(2:end);
    k = 0:(N/2)-1;
    f = (k*fs)/N; %frequency vector
    f = f(2:end);
    full = [f',X1'];
    full_sort = sortrows(full,-2);
    peaks = full_sort(1:3,1)';
    data_frequencies(i,:) = peaks;
end
%{
for i=1:len
    X = fft(test(i,2:end),N);
    X = X(1:N/2); %restricts X to positive domain only
    X1 = abs(X); %magnitude
    X1 = X1(2:end);
    k = 0:(N/2)-1;
    f = (k*fs)/N; %frequency vector
    f = f(2:end);
    full = [f',X1'];
    full_sort = sortrows(full,-2);
    peaks = full_sort(1:3,1)';
    test_frequencies(i,:) = peaks;
end
%}

for i=1:len
    temp = sort(data_full(i,2:end),'descend');
    data_maxV(i,1) = mean(temp(1:3));
    %temp2 = sort(test(i,2:end),'descend');
    %test_maxV(i,:) = temp2(1:3);
end

data_features = [data_maxV,data_frequencies(:,2)];
feats_full = [data_features,feats_full];
%test_features = [test_maxV,test_frequencies,test_means,test(:,1)];

csvwrite('final_features.txt',feats_full)
%csvwrite('test_features.txt',test_features)

%{
figure
stem(f(2:end),X1(2:end)) %does not include first large spike so we can see the actual peaks more easily
title('Magnitude spectrum')
xlabel('Frequency (Hz)')
ylabel('Abs(X(f))')
%}



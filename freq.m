clear all
train = csvread('train_full.txt');
test = csvread('test_full.txt');

fs = 500;
t_step = 1/fs;
t = 0:t_step:6-0.002;

N = 200;
X = fft(train(3,:),N);
X = X(1:N/2); %restricts X to positive domain only
X1 = abs(X); %magnitude
k = 0:(N/2)-1;
f = (k*fs)/N; %frequency vector
figure
stem(f(2:end),X1(2:end)) %does not include first large spike so we can see the actual peaks more easily
title('Magnitude spectrum')
xlabel('Frequency (Hz)')
ylabel('Abs(X(f))')


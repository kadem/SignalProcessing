clear all

cyl_ch1_full = zeros(150,3000);
cyl_ch2_full = zeros(150,3000);
hook_ch1_full = zeros(150,3000);
hook_ch2_full = zeros(150,3000);
lat_ch1_full = zeros(150,3000);
lat_ch2_full = zeros(150,3000);
palm_ch1_full = zeros(150,3000);
palm_ch2_full = zeros(150,3000);
spher_ch1_full = zeros(150,3000);
spher_ch2_full = zeros(150,3000);
tip_ch1_full = zeros(150,3000);
tip_ch2_full = zeros(150,3000);

load('sEMG_Basic_Hand_movements_upatras\Database 1\female_1.mat')

cyl_ch1_full(1:30,:) = cyl_ch1;
cyl_ch2_full(1:30,:) = cyl_ch2;
hook_ch1_full(1:30,:) = hook_ch1;
hook_ch2_full(1:30,:) = hook_ch2;
lat_ch1_full(1:30,:) = lat_ch1;
lat_ch2_full(1:30,:) = lat_ch2;
palm_ch1_full(1:30,:) = palm_ch1;
palm_ch2_full(1:30,:) = palm_ch2;
spher_ch1_full(1:30,:) = spher_ch1;
spher_ch2_full(1:30,:) = spher_ch2;
tip_ch1_full(1:30,:) = tip_ch1;
tip_ch2_full(1:30,:) = tip_ch2;

load('sEMG_Basic_Hand_movements_upatras\Database 1\female_2.mat')

cyl_ch1_full(31:60,:) = cyl_ch1;
cyl_ch2_full(31:60,:) = cyl_ch2;
hook_ch1_full(31:60,:) = hook_ch1;
hook_ch2_full(31:60,:) = hook_ch2;
lat_ch1_full(31:60,:) = lat_ch1;
lat_ch2_full(31:60,:) = lat_ch2;
palm_ch1_full(31:60,:) = palm_ch1;
palm_ch2_full(31:60,:) = palm_ch2;
spher_ch1_full(31:60,:) = spher_ch1;
spher_ch2_full(31:60,:) = spher_ch2;
tip_ch1_full(31:60,:) = tip_ch1;
tip_ch2_full(31:60,:) = tip_ch2;

load('sEMG_Basic_Hand_movements_upatras\Database 1\female_3.mat')

cyl_ch1_full(61:90,:) = cyl_ch1;
cyl_ch2_full(61:90,:) = cyl_ch2;
hook_ch1_full(61:90,:) = hook_ch1;
hook_ch2_full(61:90,:) = hook_ch2;
lat_ch1_full(61:90,:) = lat_ch1;
lat_ch2_full(61:90,:) = lat_ch2;
palm_ch1_full(61:90,:) = palm_ch1;
palm_ch2_full(61:90,:) = palm_ch2;
spher_ch1_full(61:90,:) = spher_ch1;
spher_ch2_full(61:90,:) = spher_ch2;
tip_ch1_full(61:90,:) = tip_ch1;
tip_ch2_full(61:90,:) = tip_ch2;

load('sEMG_Basic_Hand_movements_upatras\Database 1\male_1.mat')

cyl_ch1_full(91:120,:) = cyl_ch1;
cyl_ch2_full(91:120,:) = cyl_ch2;
hook_ch1_full(91:120,:) = hook_ch1;
hook_ch2_full(91:120,:) = hook_ch2;
lat_ch1_full(91:120,:) = lat_ch1;
lat_ch2_full(91:120,:) = lat_ch2;
palm_ch1_full(91:120,:) = palm_ch1;
palm_ch2_full(91:120,:) = palm_ch2;
spher_ch1_full(91:120,:) = spher_ch1;
spher_ch2_full(91:120,:) = spher_ch2;
tip_ch1_full(91:120,:) = tip_ch1;
tip_ch2_full(91:120,:) = tip_ch2;

load('sEMG_Basic_Hand_movements_upatras\Database 1\male_2.mat')

cyl_ch1_full(121:150,:) = cyl_ch1;
cyl_ch2_full(121:150,:) = cyl_ch2;
hook_ch1_full(121:150,:) = hook_ch1;
hook_ch2_full(121:150,:) = hook_ch2;
lat_ch1_full(121:150,:) = lat_ch1;
lat_ch2_full(121:150,:) = lat_ch2;
palm_ch1_full(121:150,:) = palm_ch1;
palm_ch2_full(121:150,:) = palm_ch2;
spher_ch1_full(121:150,:) = spher_ch1;
spher_ch2_full(121:150,:) = spher_ch2;
tip_ch1_full(121:150,:) = tip_ch1;
tip_ch2_full(121:150,:) = tip_ch2;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function sout = combineSounds2(len,base,Nsounds)
% sout = combineSounds2(len,base,Nsounds);

rand('state',sum(100*clock));
%bases = dryer particl2 spray shaver tear crumple coffmill

folders = strvcat('a1\cherry1','a1\cherry2','a1\cherry3','a1\wood2','a1\wood3',...
    'a2\bank','a2\bowl','a2\candybwl','a2\colacan','a2\metal15','a2\metal10','a2\metal05','a2\trashbox',...
    'a3\case1','a3\case2','a3\case3','a3\dice2','a3\dice3',...
    'a4\bottle1','a4\bottle2','a4\china3','a4\china4',...
    'b3\saw2','b3\sandpp1','b3\sandpp2',...
    'b4\sticks',...
    'b5\clap1','b5\clap2','b5\cap1','b5\cap2','b5\snap','b5\cracker',...
    'c1\bell2','c1\bells3','c1\coin2','c1\coin3',...
    'c2\book1','c2\book2',...
    'c3\castanet','c3\maracas','c3\drum',...
    'c5\stapler','c5\punch');

sout = audioread(sprintf('base%i.wav',base))';

for i = 1:Nsounds
    f = deblank(folders(ceil(rand*43),:));
    fid = -1;
    while fid == -1
        fid = fopen(sprintf('d:\\nospeech\\drysrc\\%s\\48khz\\%03i.raw',f,ceil(rand*30)),'r');
    end
    s = fread(fid,inf,'int16');
    fclose(fid);
    offset = ceil(rand*len-4800);
    s = [zeros(1,offset) s' zeros(1,len)];
    s = s(1:len)/15000;
    sout = sout + s;
end
sout = sout.*0.5;
soundsc(sout,48000);
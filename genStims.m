function genStims(o)

n = 0;
while n < 7
    s = combineSounds2(24000,o,6);
    a = input('Take?','s');
    if a
        name = sprintf('o%is%i.wav',o,n)
        s = resample(s,147,160);
        %soundsc(s,44100);
        audiowrite(s,44100,16,name);
        n = n + 1;
    end
end
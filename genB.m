% rng('default'); % does not work in octave
for x = 1:3
    fprintf("%i\n", x)
    im = rand(8,4);
    depth = rand(4,2);
    fname_write = sprintf(".99_%08d_A.mat", x);
    fname_done  = sprintf("99_%08d_.mat", x);
    % write file with locked name
    
    save('-6', fname_write, 'im', 'depth') % octave
    % save(fname_write, 'A', '-v6') % matlab

    pause(2);
    % rename
    movefile(fname_write,fname_done);
end

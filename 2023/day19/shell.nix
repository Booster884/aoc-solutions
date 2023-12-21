{ pkgs ? import <nixpkgs> { system = builtins.currentSystem; } }:

pkgs.mkShell {
    packages = [
        (pkgs.python311.withPackages (ps: [
            ps.lark
        ]))
    ];
}

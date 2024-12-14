{
  description = "build text-speech";

  inputs = {
    nixpkgs.url = "github:ahbk/nixpkgs/nixos-unstable";

  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          (pkgs.python3.withPackages (
            python-pkgs: with python-pkgs; [
              google-cloud-texttospeech
            ]
          ))
        ];
      };
    };
}

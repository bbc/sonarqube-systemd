# SonarQube systemd

**Easily package the SonarQube Community Edition and install it as a systemd service.**

## Getting started as a developer

### Building as an RPM

Clone the repository and navigate to the `rpm` directory in a terminal.

Make sure the `rpmbuild` and `createrepo` commands are available on your system. If they aren't, you will need to install them with commands similar to the following:
```
yum install rpm-build
yum install createrepo
```

To build the RPM, simply run:
```
make VERSION=7.9
```
Of course, feel free to adjust the version number to suit your needs.

The deployable repository will be created in the `repo` folder.

## Contributing

#### `$ code`

This project was built by [Pierre-Yves](https://github.com/PyvesB) during a BBC hackathon. Contributions are more than welcome, open a **pull request** and share your code! Simply **fork** the repository by clicking on the icon on the top right of this page and you're ready to go!

#### :speech_balloon: Support

Thought of a cool idea? Found a problem or need some help? Simply open an [**issue**](https://github.com/bbc/sonarqube-packages/issues)!

#### :star: Thanks

Find the project useful, fun or interesting? **Star** the repository by clicking on the icon on the top right of this page!

## Acknowledgements

The following open-source tools are central part of this project:
* [SonarQube](https://github.com/SonarSource/sonarqube), released by SonarSource under the [LGPL-3.0 License](https://github.com/SonarSource/sonarqube/blob/master/LICENSE.txt).
* [systemd](https://github.com/systemd/systemd), released under the [LGPL-2. License](https://github.com/systemd/systemd/blob/master/LICENSE.LGPL2.1).

## License and copyright

Apache License 2.0, see [LICENSE](https://github.com/bbc/sonarqube-packages/blob/master/LICENSE) for more details.

Copyright 2019 British Broadcasting Corporation

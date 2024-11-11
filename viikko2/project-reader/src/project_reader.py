from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deserialised = loads(content)["tool"]["poetry"]

        name = deserialised["name"]
        description = deserialised["description"]
        license = deserialised["license"]
        authors = deserialised["authors"]
        dependencies = list(deserialised["dependencies"])
        dev_dependencies = list(deserialised["group"]["dev"]["dependencies"])
        
        return Project(name, description, license, authors, dependencies, dev_dependencies)

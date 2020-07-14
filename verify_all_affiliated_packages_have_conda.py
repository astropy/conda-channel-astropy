# Check that every affiliated package is listed in requirements.yml

import yaml

import requests
from binstar_client.utils import get_server_api
from binstar_client import NotFound

AFFILIATED_PACKAGES_LIST = 'http://www.astropy.org/affiliated/registry.json'
REQUIREMENTS = 'requirements.yml'


def check_for_omitted_packages():
    """
    Return a list of any affiliated packages not listed in requirements
    """

    pkg_list = requests.get(AFFILIATED_PACKAGES_LIST).json()
    with open(REQUIREMENTS, 'rt') as f:
        reqs_list = yaml.safe_load(f)
    packge_list_names = set([p['pypi_name'].lower() for p in pkg_list['packages']])
    requirements_names = set([r['name'].lower() for r in reqs_list])

    # Construct list of packages in the registry that are not in the astropy
    # conda-forge channel.
    missing = packge_list_names - requirements_names
    api = get_server_api()
    add_to_requirements = []
    make_recipe = []

    # Check whether missing packages are already on conda-forge
    for package in sorted(missing):
        try:
            api.package('conda-forge', package)
        except NotFound:
            on_conda_forge = False
        else:
            on_conda_forge = True

        if on_conda_forge:
            add_to_requirements.append(package)
        else:
            make_recipe.append(package)

    if add_to_requirements:
        print("\n\nCopy/paste this into requirements.yml:\n\n")
        print("\n\n".join([f"- name: {package}" for package in add_to_requirements]))

    if make_recipe:
        print("\n\nMake a new conda recipe on conda-forge for each of these:")
        print("\n".join(make_recipe))
        print("\n\n")


if __name__ == "__main__":
    check_for_omitted_packages()

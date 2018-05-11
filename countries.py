"""Look up formal country names

Todo:

https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages

"""

import re
import pycountry


_COUNTRY_MAPPINGS = {
    'Cape Verde': 'Cabo Verde',
    'Democratic Republic of the Congo': 'Congo, The Democratic Republic of the',
    'Holy See': 'Holy See (Vatican City State)',
    'Libyan Arab Jamahiriya': 'Libya',
}


_NON_STATE_PARTICIPANTS = {
    'world health organization': 'World Health Organization',
    'european onion': 'European Union'
}


def normalize(country):

    # Try to lookup country name as given
    try:
        return pycountry.countries.lookup(country)
    except LookupError:
        print(country)

    # Remove numbers and parentheses
    country_name = country.replace(' (', ', ').replace('St.', 'Saint')
    country_name = re.sub(r'[0-9)(\[\]]', '', country_name).strip()
    while country_name.endswith(','):
        country_name = country_name[:-1].strip()
    print(f"{country} -> {country_name}")
    try:
        return pycountry.countries.lookup(country_name)
    except LookupError:
        pass
    
    # Yoda, Write Like
    words = country_name.split()
    country_with_comma = f"{words[-1]}, {' '.join(words[:-1])}"
    print(f"{country} -> {country_name} -> {country_with_comma}")
    try:
        return pycountry.countries.lookup(country_with_comma)
    except LookupError:
        pass

    # "While the EU is an observer, it is party to some 50 international UN agreements as the only non-state participant"
    # https://en.wikipedia.org/wiki/United_Nations_General_Assembly_observers#European_Union
    try:
        mapped_country_name = _NON_STATE_PARTICIPANTS[country_name.lower()]
        print(f"{country} -> (observer, non-state participant) -> {mapped_country_name} ")
        return mapped_country_name
    except KeyError:
        pass
    
    # Use manual mapping
    try:
        mapped_country_name = _COUNTRY_MAPPINGS[country_name]
    except KeyError:
        # import IPython; IPython.embed()
        mapped_country_name = 'Not found in _COUNTRY_MAPPINGS'
    print(f"{country} -> {country_name} -> {mapped_country_name}")
    return pycountry.countries.lookup(mapped_country_name)



def old_stuff():
    pattern = re.compile(r'[,0-9)(\[\]]')   # Only keep letters and spaces
    normalized = list()

    for country in countries:
        try:
            country_name = pattern.sub('', country).strip()
        except TypeError:
            normalized.append('No country')
            continue

        try:
            codes = pycountry.countries.lookup(country_name)
            normalized.append(codes.alpha_3)
        except LookupError:
            # TODO: Do a second more manual search through pycountry
            normalized.append(country_name)

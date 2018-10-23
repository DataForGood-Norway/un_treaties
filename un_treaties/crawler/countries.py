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
    'Eswatini':'Swaziland',
}


_NON_STATE_PARTICIPANTS = {
    'world health organization': 'World Health Organization',
    'european union': 'European Union',
    'council of europe': 'Council of Europe',
    'andean community': 'Andean Community',
    'caribbean community': 'Caribbean Community',
    'common market for eastern and southern africa': 'Common Market for Eastern and Southern Africa',
    'east african community': 'East African Community',
    'economic community of west african states': 'Economic Community of West African States',
    'eurasian economic community': 'Eurasian Economic Community',
    'organization of african unity': 'Organization of African Unity',
    'southern african development community': 'Southern African Development Community',
    'west african economic and monetary union': 'West African Economic and Monetary Union',
    'food and agriculture organization of the united nations': 'Food and Agriculture Organization of the UN',
}


def normalize(country):

    # Try to lookup country name as given
    try:
        return pycountry.countries.lookup(country).name
    except LookupError:
        # print(country)
        pass

    # Remove numbers and parentheses
    country_name = country.replace(' (', ', ').replace('St.', 'Saint')
    country_name = re.sub(r'[0-9)(\[\]]', '', country_name).strip()
    while country_name.endswith(','):
        country_name = country_name[:-1].strip()
    # print(f"{country} -> {country_name}")
    try:
        return pycountry.countries.lookup(country_name).name
    except LookupError:
        pass

    # Yoda, Write Like
    words = country_name.split()
    country_with_comma = f"{words[-1]}, {' '.join(words[:-1])}"
    # print(f"{country} -> {country_name} -> {country_with_comma}")
    try:
        return pycountry.countries.lookup(country_with_comma).name
    except LookupError:
        pass

    # Use manual mapping
    try:
        mapped_country_name = _COUNTRY_MAPPINGS[country_name]
        return pycountry.countries.lookup(mapped_country_name).name
    except KeyError:
        pass
        # import IPython; IPython.embed()
        # print(f"{country} -> {country_name} -> {mapped_country_name}")

    # "While the EU is an observer, it is party to some 50 international UN agreements as the only non-state participant"
    # https://en.wikipedia.org/wiki/United_Nations_General_Assembly_observers#European_Union
    mapped_country_name = _NON_STATE_PARTICIPANTS.get(country_name.lower(), country_name)
    # print(f"{country} -> (observer, non-state participant) -> {mapped_country_name} ")
    return mapped_country_name


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

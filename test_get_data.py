import unittest
import get_data

#BASE = 'https://treaties.un.org/Pages/'
#START_PAGE = 'ParticipationStatus.aspx?clang=_en'

class TestGetData(unittest.TestCase):


    # easy case, already parsed correctly
    def test_url01(self):
        self.maxDiff = None
        self.url = 'https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=VI-1&chapter=6&clang=_en'
        self.output = dict(
            entryForce='11 December 1946, in accordance with article VII(1).',
            registration='3 February 1948, No. 186',
            status='Signatories : 23. Parties : 62',
            pdf='United Nations, Treaty Series , vol. 12, p. 179.',
            Treaty='1. Protocol amending the Agreements, Conventions and Protocols on Narcotic Drugs, concluded at The Hague on 23 January 1912, at Geneva on 11 February 1925 and 19 February 1925, and 13 July 1931, at Bangkok on 27 November 1931 and at Geneva on 26 June 1936',
            Chapter='NARCOTIC DRUGS AND PSYCHOTROPIC SUBSTANCES',
            Date='Lake Success, New York, 11 December 1946'
        )
        self.assertCountEqual(get_data.read_header_treaty(self.url).keys(),
                              self.output.keys())
        self.assertDictEqual(get_data.read_header_treaty(self.url),
                             self.output)

    ## problem finding "Participant" in table
    def test_url02(self):
        self.url = get_data.BASE + 'ViewDetails.aspx?src=TREATY&mtdsg_no=I-5-a&chapter=1&clang=_en'
        print(self.url)        
        self.output = dict(
            entryForce='31 August 1965, in accordance with article 108for all Members of the United Nations. 2',
            registration='1 March 1966, No. 8132',
            status='Parties : 107',
            pdf='United Nations, Treaty Series, vol. 557, p. 143.',
            Treaty='5. a Amendments to Articles 23, 27 and 61 of the Charter of the United Nations, adopted by the General Assembly of the United Nations in resolutions 1991 A and B (XVIII) of 17 December 1963',
            Chapter='CHARTER OF THE UNITED NATIONS AND STATUTE OF THE INTERNATIONAL COURT OF JUSTICE',
            Date='New York, 17 December 1963 1'
        )
        print(get_data.read_header_treaty(self.url))
        self.assertDictEqual(get_data.read_header_treaty(self.url),
                             self.output)

if __name__ == '__main__':
    unittest.main()

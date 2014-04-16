Methods available
=================

**FauxFactory.generate_alpha( length=5 )**
    Generates an random alpha string of the size of the given ``length``. ::

        >>>FauxFactory.generate_alpha( )
        CIeuB
        >>>FauxFactory.generate_alpha(10)
        YPTgKEtjKd

|

**FauxFactory.generate_alphanumeric( length=5 )**
    Generates an random alphanumeric string of the size of the given ``length``.

|

**FauxFactory.generate_boolean( )**
    Generates a random boolean value.

|

**FauxFactory.generate_choice( choices )**
    Generates a random choice based on the given ``choices``. ::

        >>>my_list = ['John', 'Paul', 'Philip']
        >>>FauxFactory.generate_choice( my_list )
        'Paul'
        >>>my_tuple = (1,2,3,4,5)
        >>>FauxFactory.generate_choice( my_tuple )
        2

|

**FauxFactory.generate_cjk( length=5 )**
    Generates a random string of the size of the given ``length`` made up of the CJK characters.

|

**FauxFactory.generate_date( min_date=None, max_date=None )**
    Generates a random date between ``min_date`` and ``max_date``. Both parameters must be instances of datetime.date. ::

        >>>min_date = datetime.date(2014, 01, 01)
        >>>max_date = datetime.date(2014, 05, 01)
        >>>print FauxFactory.generate_date( min_date, max_date )
        2014-02-13
        >>>print FauxFactory.generate_date( )
        2894-07-17

|

**FauxFactory.generate_datetime( min_date=None, max_date=None )**
    Generates a random datetime value between ``min_date`` and ``max_date``.

|

**FauxFactory.generate_email( name=None, domain=None, tlds=None )**
    Generates a random email according to the given ``name``,
    ``domain`` and ``tlds``(Top Level Domain Server).

 ::

        >>>FauxFactory.generate_email('ozzy')
        ozzy@test.com
        >>FauxFactory.generate_email(name='paul', domain='mycompany')
        paul@company.biz

|

**FauxFactory.generate_integer( min_value=None, max_value=None )**
    Generates a random integer number betweeen ``min_value`` and ``max_value``. ::

        >>>FauxFactory.generate_integer(1, 10)
        5
        >>>FauxFactory.generate_integer()
        2395249348247495256

|

**FauxFactory.generate_ipaddr( ip3=False, ipv6=False )**
    Generates a random ip address. ::

        >>>FauxFactory.generate_ipaddr( )
        13.169.231.199
        >>>FauxFactory.generate_ipaddr(ip3=True)
        165.209.148.0
        >>>FauxFactory.generate_ipaddr(ipv6=True)
        adab:a917:3226:c64b:8d02:cceb:c212:be9d

|

**FauxFactory.generate_latin1( length=5 )**
    Generates a random string encoded in latin1 of size of the given ``length``.

|

**FauxFactory.generate_mac( delimiter=":" )**
    Generates a random mac addrees based on the given ``delimiter``.
    Accepted values for ``delimiter`` are: 
        - ':'
        - '-' ::

            >>>FauxFactory.generate_mac()
            52:86:af:33:79:83
            >>>FauxFactory.generate_mac("-")
            9a-7a-a8-42-4f-fe

|

**FauxFactory.generate_negative_integer( )**
    Generates a random negative integer number.

|

**FauxFactory.generate_numeric_string( length=5 )**
    Generates a random numeric string of the size of ``length``.

|

**FauxFactory.generate_positive_integer( )**
    Generates a random positive integer number.

|

**FauxFactory.generate_string( str_type, length )**
    Generates a random string according to the given ``str_type`` and ``length``.
    Accepted values for parameter ``str_type`` are: 
        - 'alphanumeric'                                                   
        - 'alpha'                                                          
        - 'latin1'                                                         
        - 'numeric'                                                        
        - 'utf8' ::

            >>>FauxFactory.generate_string('alphanumeric', 10)
            vhErvQKP3G
            >>>FauxFactory.generate_string('alpha', 20)
            PEIZvevsWZllMGmClnvf
            >>>FauxFactory.generate_string('numeric', 5)
            11356

|

**FauxFactory.generate_time( )**
    Generates a random time. The output will be an instance of datetime.time class.

|

**FauxFactory.generate_url( scheme=None, subdomain=None, tlds=None )**
    Generates a random url based on the given ``scheme``, ``subdomain`` and ``tlds``.
    Accepted values for parameter ``scheme`` are:
        - 'http'
        - 'https'
        - 'ftp' ::

            >>>FauxFactory.generate_url()
            http://test.biz
            >>>FauxFactory.generate_url(scheme='https')
            https://example.org
            >>>FauxFactory.generate_url(scheme='ftp', subdomain='mycompany')
            ftp://mycompany.biz

|

**FauxFactory.generate_uuid( )**
    Generates a random uuid - Universal Unique Identifier

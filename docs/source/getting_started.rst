Getting Started
====================

FauxFactory is a tool written in python that helps you generate ramdom data to your automated tests!

Need a 10 characters string for one of your tests? ::

    >>>FauxFacotry.generate_string('alphanumeric', 10)
    fkQcdGGfH1

Need a 5 character numeric string? ::

    >>>FauxFactory.generate_string('numeric', 5)
    14354

Simple, right?

Now, let's say you need random dates ::

    >>>FauxFactory.generate_date()
    2972-02-26

and a fake email ::

    >>>FauxFactory.generate_email()
    BYZDADvs@test.biz


Methods available
-----------------

**FauxFactory.generate_alpha( length=5 )**
    Generates an random alpha string of the size of the given length. ::

        >>>FauxFactory.generate_alpha( )
        CIeuB
        >>>FauxFactory.generate_alpha(10)
        YPTgKEtjKd


**FauxFactory.generate_alphanumeric( length=5 )**
    Generates an random alphanumeric string of the size of the given length.


**FauxFactory.generate_boolean( )**
    Generates a random boolean value.


**FauxFactory.generate_choice( choices )**
    Generates a random choice based on the given choices. ::

        >>>my_list = ['Jhon', 'Paul', 'Philip']
        >>>FauxFactory.generate_choice( my_list )
        'Paul'

        >>>my_tuple = (1,2,3,4,5)
        >>>FauxFactory.generate_choice( my_tuple )
        2


**FauxFactory.generate_cjk( )**
    Generates a random string of the size of the given length made up of the CJK characters.


**FauxFactory.generate_date( min_date=None, max_date=None )**


**FauxFactory.generate_datetime( min_date=None, max_date=None )**


**FauxFactory.generate_email( name=None, domain=None, tlds=None )**


**FauxFactory.generate_integer( min_value=None, max_value=None )**


**FauxFactory.generate_ipaddr( ip3=False, ipv6=False )**


**FauxFactory.generate_latin1( length=5 )**
    Generates a random string encoded in latin1 of size of the given length


**FauxFactory.generate_mac( delimiter=":" )**


**FauxFactory.generate_negative_integer( )**


**FauxFactory.generate_numeric_string( length=5 )**


**FauxFactory.generate_positive_integer( )**


**FauxFactory.generate_string( type, length=5 )**
    Generates a random string according to the given ``type`` and ``length``.
    Accpeted values for the parameter ``type`` are: 
        - "alphanumeric"                                                   
        - "alpha"                                                          
        - "latin1"                                                         
        - "numeric"                                                        
        - "utf8"                                                           


**FauxFactory.generate_time( )**


**FauxFactory.generate_url( scheme=None, subdomain=None, tlds=None )**


**FauxFactory.generate_uuid( )**


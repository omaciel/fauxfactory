Getting Started
====================

FauxFactory generates random data for your automated tests easily!

Need a 10 characters string for one of your tests? ::

    >>>FauxFacotry.generate_string('alphanumeric', 10)
    fkQcdGGfH1

Need a 5 character numeric string? ::

    >>>FauxFactory.generate_string('numeric', 5)
    14354

Now, let's say you need a random date ::

    >>>FauxFactory.generate_date()
    2972-02-26

and a fake email with your company domain ::

    >>>FauxFactory.generate_email(domain="mycompany")
    ZniSxAvb@mycompany.com

Simple, right?

|

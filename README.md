[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/16.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/16.0/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/16.0/developer/howtos.html">the developer tutorials</a>


Guide for custom searching

- Step 1:
  - Open query console on postgresql
  - Run query 'CREATE EXTENSION unaccent;
             SELECT unaccent('Hôtel');'
- Step 2:
  - Run pip install cmd:'pip install unidecode'
- Step 3:
  - add to patient.py model '
    name = fields.Char(string='Name', required=True, tracking=True, help='This is the name of the patient') # đây là trường show ra
    name_unaccent = fields.Char(string='Name Unaccent', compute='_compute_name_unaccent', store=True) # đây là trường dùng cho tìm kiếm không dấu

    @api.depends('name')
    def _compute_name_unaccent(self): # đây là function cho việc thực hiện query tìm kiếm
        for record in self:
            record.name_unaccent = unidecode(record.name).lower() if record.name else ''

'

- Step 4: add to patient.xml:
  "
<search>
	<field name="name" filter_domain="['|', ('name_unaccent', 'ilike', '%'+self+'%'), ('ref', 'ilike', self)]"/>
</search>
  "


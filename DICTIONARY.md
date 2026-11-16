# dol-visas Data Dictionary

Built from DOL OFLC quarterly disclosure files (https://www.dol.gov/agencies/eta/foreign-labor/performance).
Column availability varies by fiscal-year era; see crosswalk_lca.csv and crosswalk_perm.csv in the build repo for the exact per-era source-column mappings and every documented drop.

## lca

H-1B/H-1B1/E-3 Labor Condition Applications, one row per application per disclosure file, FY2015-present. 7,596,060 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_address1` | VARCHAR | 52.0% | 	1400 Broadway |
| `agent_attorney_address1` | VARCHAR | 52.0% | 	1400 Broadway |
| `agent_attorney_address2` | VARCHAR | 62.4% | 	STE 102 |
| `agent_attorney_address2` | VARCHAR | 62.4% | 	STE 102 |
| `agent_attorney_city` | VARCHAR | 30.7% | ,Croton |
| `agent_attorney_city` | VARCHAR | 30.7% | ,Croton |
| `agent_attorney_country` | VARCHAR | 52.0% | AFGHANISTAN |
| `agent_attorney_country` | VARCHAR | 52.0% | AFGHANISTAN |
| `agent_attorney_email_address` | VARCHAR | 57.8% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_email_address` | VARCHAR | 57.8% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_first_name` | VARCHAR | 57.8% | (Rachel) Ji-Young |
| `agent_attorney_first_name` | VARCHAR | 57.8% | (Rachel) Ji-Young |
| `agent_attorney_last_name` | VARCHAR | 57.8% | (Swett) Smith |
| `agent_attorney_last_name` | VARCHAR | 57.8% | (Swett) Smith |
| `agent_attorney_middle_name` | VARCHAR | 76.3% | & |
| `agent_attorney_middle_name` | VARCHAR | 76.3% | & |
| `agent_attorney_name` | VARCHAR | 69.5% | (DAVID) LIHWEI LIN |
| `agent_attorney_name` | VARCHAR | 69.5% | (DAVID) LIHWEI LIN |
| `agent_attorney_phone` | VARCHAR | 52.0% | +10013236534514 |
| `agent_attorney_phone` | VARCHAR | 52.0% | +10013236534514 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 52.0% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 52.0% | 0 |
| `agent_attorney_province` | VARCHAR | 93.6% | (213) 384-1900 |
| `agent_attorney_province` | VARCHAR | 93.6% | (213) 384-1900 |
| `agent_attorney_state` | VARCHAR | 33.1% | AK |
| `agent_attorney_state` | VARCHAR | 33.1% | AK |
| `agent_representing_employer` | VARCHAR | 18.3% | N |
| `agent_representing_employer` | VARCHAR | 18.3% | N |
| `agree_to_lc_statement` | VARCHAR | 35.9% | N |
| `agree_to_lc_statement` | VARCHAR | 35.9% | N |
| `amended_petition` | INTEGER | 16.7% | 0 |
| `amended_petition` | INTEGER | 16.7% | 0 |
| `appendix_a_attached` | VARCHAR | 42.4% | N/A |
| `appendix_a_attached` | VARCHAR | 42.4% | N/A |
| `begin_date` | DATE | 0.0% | 2008-04-09 |
| `begin_date` | DATE | 0.0% | 2008-04-09 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `change_employer` | INTEGER | 16.7% | 0 |
| `change_employer` | INTEGER | 16.7% | 0 |
| `change_previous_employment` | INTEGER | 16.7% | 0 |
| `change_previous_employment` | INTEGER | 16.7% | 0 |
| `continued_employment` | INTEGER | 16.7% | 0 |
| `continued_employment` | INTEGER | 16.7% | 0 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address2` | VARCHAR | 61.5% | 					 |
| `employer_address2` | VARCHAR | 61.5% | 					 |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_country` | VARCHAR | 1.6% | AFGHANISTAN |
| `employer_country` | VARCHAR | 1.6% | AFGHANISTAN |
| `employer_fein` | VARCHAR | 77.5% | 01-0020240 |
| `employer_fein` | VARCHAR | 77.5% | 01-0020240 |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_phone` | VARCHAR | 1.6% | (516363587 |
| `employer_phone` | VARCHAR | 1.6% | (516363587 |
| `employer_phone_ext` | VARCHAR | 94.1% | (716) 8 |
| `employer_phone_ext` | VARCHAR | 94.1% | (716) 8 |
| `employer_poc_address1` | VARCHAR | 48.7% | 	  600 Harrison Street |
| `employer_poc_address1` | VARCHAR | 48.7% | 	  600 Harrison Street |
| `employer_poc_address2` | VARCHAR | 74.7% | 	 |
| `employer_poc_address2` | VARCHAR | 74.7% | 	 |
| `employer_poc_address_1` | VARCHAR | 93.6% | 	1000  ASU Drive |
| `employer_poc_address_1` | VARCHAR | 93.6% | 	1000  ASU Drive |
| `employer_poc_address_2` | VARCHAR | 96.7% | 	 |
| `employer_poc_address_2` | VARCHAR | 96.7% | 	 |
| `employer_poc_city` | VARCHAR | 42.3% | 	 Jersey City |
| `employer_poc_city` | VARCHAR | 42.3% | 	 Jersey City |
| `employer_poc_country` | VARCHAR | 42.3% | AFGHANISTAN |
| `employer_poc_country` | VARCHAR | 42.3% | AFGHANISTAN |
| `employer_poc_email` | VARCHAR | 42.3% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_email` | VARCHAR | 42.3% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_first_name` | VARCHAR | 42.3% | 	 Belinda |
| `employer_poc_first_name` | VARCHAR | 42.3% | 	 Belinda |
| `employer_poc_job_title` | VARCHAR | 42.3% | 	$151154.00 |
| `employer_poc_job_title` | VARCHAR | 42.3% | 	$151154.00 |
| `employer_poc_last_name` | VARCHAR | 42.3% | 	Arnaudez |
| `employer_poc_last_name` | VARCHAR | 42.3% | 	Arnaudez |
| `employer_poc_middle_name` | VARCHAR | 84.3% | 	 |
| `employer_poc_middle_name` | VARCHAR | 84.3% | 	 |
| `employer_poc_phone` | VARCHAR | 42.3% | +0012172214634 |
| `employer_poc_phone` | VARCHAR | 42.3% | +0012172214634 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_postal_code` | VARCHAR | 42.3% | 00-815 |
| `employer_poc_postal_code` | VARCHAR | 42.3% | 00-815 |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_state` | VARCHAR | 42.3% | AK |
| `employer_poc_state` | VARCHAR | 42.3% | AK |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 83.2% | "N/A" |
| `employer_province` | VARCHAR | 83.2% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_state` | VARCHAR | 0.0% | AK |
| `end_date` | DATE | 0.0% | 2010-08-10 |
| `end_date` | DATE | 0.0% | 2010-08-10 |
| `full_time_position` | VARCHAR | 8.5% | N |
| `full_time_position` | VARCHAR | 8.5% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `lawfirm_business_fein` | VARCHAR | 89.8% | 01-0000000 |
| `lawfirm_business_fein` | VARCHAR | 89.8% | 01-0000000 |
| `lawfirm_name_business_name` | VARCHAR | 51.9% | (201)489-1351 |
| `lawfirm_name_business_name` | VARCHAR | 51.9% | (201)489-1351 |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `name_of_highest_state_court` | VARCHAR | 52.1% | 	CA Supreme Court |
| `name_of_highest_state_court` | VARCHAR | 52.1% | 	CA Supreme Court |
| `new_concurrent_emp` | VARCHAR | 91.4% | 0 |
| `new_concurrent_emp` | VARCHAR | 91.4% | 0 |
| `new_concurrent_employment` | INTEGER | 25.3% | 0 |
| `new_concurrent_employment` | INTEGER | 25.3% | 0 |
| `new_employment` | INTEGER | 16.7% | 0 |
| `new_employment` | INTEGER | 16.7% | 0 |
| `original_cert_date` | DATE | 94.5% | 2009-07-29 |
| `original_cert_date` | DATE | 94.5% | 2009-07-29 |
| `preparer_business_name` | VARCHAR | 70.4% | (678) 553-7349 |
| `preparer_business_name` | VARCHAR | 70.4% | (678) 553-7349 |
| `preparer_email` | VARCHAR | 70.3% | 	juan.mata@balglobal.com |
| `preparer_email` | VARCHAR | 70.3% | 	juan.mata@balglobal.com |
| `preparer_first_name` | VARCHAR | 70.4% | 	Kiranmai |
| `preparer_first_name` | VARCHAR | 70.4% | 	Kiranmai |
| `preparer_last_name` | VARCHAR | 70.4% | 	Pittakadapala |
| `preparer_last_name` | VARCHAR | 70.4% | 	Pittakadapala |
| `preparer_middle_initial` | VARCHAR | 87.2% | $ |
| `preparer_middle_initial` | VARCHAR | 87.2% | $ |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `public_disclosure` | VARCHAR | 34.0% | BOTH |
| `public_disclosure` | VARCHAR | 34.0% | BOTH |
| `pw_oes_year` | INTEGER | 98.9% | 1 |
| `pw_oes_year` | INTEGER | 98.9% | 1 |
| `pw_other_source` | VARCHAR | 95.0% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_source` | VARCHAR | 95.0% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_survey_name` | VARCHAR | 96.5% | 	Radford Global Technology Survey |
| `pw_survey_name` | VARCHAR | 96.5% | 	Radford Global Technology Survey |
| `pw_survey_publisher` | VARCHAR | 96.4% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_survey_publisher` | VARCHAR | 96.4% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_wage_level` | VARCHAR | 16.2% | I |
| `pw_wage_level` | VARCHAR | 16.2% | I |
| `pw_wage_source` | VARCHAR | 66.5% | CBA |
| `pw_wage_source` | VARCHAR | 66.5% | CBA |
| `pw_wage_source_other` | VARCHAR | 66.7% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_other` | VARCHAR | 66.7% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_year` | INTEGER | 66.5% | 0 |
| `pw_wage_source_year` | INTEGER | 66.5% | 0 |
| `received_date` | DATE | 0.0% | 2009-07-28 |
| `received_date` | DATE | 0.0% | 2009-07-28 |
| `secondary_entity` | VARCHAR | 34.6% | N |
| `secondary_entity` | VARCHAR | 34.6% | N |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `state_of_highest_court` | VARCHAR | 52.1% | /COURT OF APPEALS |
| `state_of_highest_court` | VARCHAR | 52.1% | /COURT OF APPEALS |
| `statutory_basis` | VARCHAR | 81.8% | $60,000 or higher annual wage |
| `statutory_basis` | VARCHAR | 81.8% | $60,000 or higher annual wage |
| `support_h1b` | VARCHAR | 23.7% | N |
| `support_h1b` | VARCHAR | 23.7% | N |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worksite_locations` | INTEGER | 42.4% | 1 |
| `total_worksite_locations` | INTEGER | 42.4% | 1 |
| `trade_name_dba` | VARCHAR | 85.4% | 	 |
| `trade_name_dba` | VARCHAR | 85.4% | 	 |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 49.8% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 49.8% | 0.0 |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `willful_violator` | VARCHAR | 2.3% | N |
| `willful_violator` | VARCHAR | 2.3% | N |
| `worksite_address1` | VARCHAR | 34.0% | 		1960 Ivy Creek Blvd |
| `worksite_address1` | VARCHAR | 34.0% | 		1960 Ivy Creek Blvd |
| `worksite_address2` | VARCHAR | 79.9% | 	 |
| `worksite_address2` | VARCHAR | 79.9% | 	 |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_county` | VARCHAR | 1.3% | #47644 OAKLAND MACOMB |
| `worksite_county` | VARCHAR | 1.3% | #47644 OAKLAND MACOMB |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_workers` | INTEGER | 34.8% | 1 |
| `worksite_workers` | INTEGER | 34.8% | 1 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 42.3% | Q1 |
| `quarter` | VARCHAR | 42.3% | Q1 |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |
| `is_latest` | BOOLEAN | 0.0% | false |
| `agent_attorney_address1` | VARCHAR | 52.0% | 	1400 Broadway |
| `agent_attorney_address1` | VARCHAR | 52.0% | 	1400 Broadway |
| `agent_attorney_address2` | VARCHAR | 62.4% | 	STE 102 |
| `agent_attorney_address2` | VARCHAR | 62.4% | 	STE 102 |
| `agent_attorney_city` | VARCHAR | 30.7% | ,Croton |
| `agent_attorney_city` | VARCHAR | 30.7% | ,Croton |
| `agent_attorney_country` | VARCHAR | 52.0% | AFGHANISTAN |
| `agent_attorney_country` | VARCHAR | 52.0% | AFGHANISTAN |
| `agent_attorney_email_address` | VARCHAR | 57.8% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_email_address` | VARCHAR | 57.8% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_first_name` | VARCHAR | 57.8% | (Rachel) Ji-Young |
| `agent_attorney_first_name` | VARCHAR | 57.8% | (Rachel) Ji-Young |
| `agent_attorney_last_name` | VARCHAR | 57.8% | (Swett) Smith |
| `agent_attorney_last_name` | VARCHAR | 57.8% | (Swett) Smith |
| `agent_attorney_middle_name` | VARCHAR | 76.3% | & |
| `agent_attorney_middle_name` | VARCHAR | 76.3% | & |
| `agent_attorney_name` | VARCHAR | 69.5% | (DAVID) LIHWEI LIN |
| `agent_attorney_name` | VARCHAR | 69.5% | (DAVID) LIHWEI LIN |
| `agent_attorney_phone` | VARCHAR | 52.0% | +10013236534514 |
| `agent_attorney_phone` | VARCHAR | 52.0% | +10013236534514 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 52.0% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 52.0% | 0 |
| `agent_attorney_province` | VARCHAR | 93.6% | (213) 384-1900 |
| `agent_attorney_province` | VARCHAR | 93.6% | (213) 384-1900 |
| `agent_attorney_state` | VARCHAR | 33.1% | AK |
| `agent_attorney_state` | VARCHAR | 33.1% | AK |
| `agent_representing_employer` | VARCHAR | 18.3% | N |
| `agent_representing_employer` | VARCHAR | 18.3% | N |
| `agree_to_lc_statement` | VARCHAR | 35.9% | N |
| `agree_to_lc_statement` | VARCHAR | 35.9% | N |
| `amended_petition` | INTEGER | 16.7% | 0 |
| `amended_petition` | INTEGER | 16.7% | 0 |
| `appendix_a_attached` | VARCHAR | 42.4% | N/A |
| `appendix_a_attached` | VARCHAR | 42.4% | N/A |
| `begin_date` | DATE | 0.0% | 2008-04-09 |
| `begin_date` | DATE | 0.0% | 2008-04-09 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `change_employer` | INTEGER | 16.7% | 0 |
| `change_employer` | INTEGER | 16.7% | 0 |
| `change_previous_employment` | INTEGER | 16.7% | 0 |
| `change_previous_employment` | INTEGER | 16.7% | 0 |
| `continued_employment` | INTEGER | 16.7% | 0 |
| `continued_employment` | INTEGER | 16.7% | 0 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address2` | VARCHAR | 61.5% | 					 |
| `employer_address2` | VARCHAR | 61.5% | 					 |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_country` | VARCHAR | 1.6% | AFGHANISTAN |
| `employer_country` | VARCHAR | 1.6% | AFGHANISTAN |
| `employer_fein` | VARCHAR | 77.5% | 01-0020240 |
| `employer_fein` | VARCHAR | 77.5% | 01-0020240 |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_phone` | VARCHAR | 1.6% | (516363587 |
| `employer_phone` | VARCHAR | 1.6% | (516363587 |
| `employer_phone_ext` | VARCHAR | 94.1% | (716) 8 |
| `employer_phone_ext` | VARCHAR | 94.1% | (716) 8 |
| `employer_poc_address1` | VARCHAR | 48.7% | 	  600 Harrison Street |
| `employer_poc_address1` | VARCHAR | 48.7% | 	  600 Harrison Street |
| `employer_poc_address2` | VARCHAR | 74.7% | 	 |
| `employer_poc_address2` | VARCHAR | 74.7% | 	 |
| `employer_poc_address_1` | VARCHAR | 93.6% | 	1000  ASU Drive |
| `employer_poc_address_1` | VARCHAR | 93.6% | 	1000  ASU Drive |
| `employer_poc_address_2` | VARCHAR | 96.7% | 	 |
| `employer_poc_address_2` | VARCHAR | 96.7% | 	 |
| `employer_poc_city` | VARCHAR | 42.3% | 	 Jersey City |
| `employer_poc_city` | VARCHAR | 42.3% | 	 Jersey City |
| `employer_poc_country` | VARCHAR | 42.3% | AFGHANISTAN |
| `employer_poc_country` | VARCHAR | 42.3% | AFGHANISTAN |
| `employer_poc_email` | VARCHAR | 42.3% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_email` | VARCHAR | 42.3% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_first_name` | VARCHAR | 42.3% | 	 Belinda |
| `employer_poc_first_name` | VARCHAR | 42.3% | 	 Belinda |
| `employer_poc_job_title` | VARCHAR | 42.3% | 	$151154.00 |
| `employer_poc_job_title` | VARCHAR | 42.3% | 	$151154.00 |
| `employer_poc_last_name` | VARCHAR | 42.3% | 	Arnaudez |
| `employer_poc_last_name` | VARCHAR | 42.3% | 	Arnaudez |
| `employer_poc_middle_name` | VARCHAR | 84.3% | 	 |
| `employer_poc_middle_name` | VARCHAR | 84.3% | 	 |
| `employer_poc_phone` | VARCHAR | 42.3% | +0012172214634 |
| `employer_poc_phone` | VARCHAR | 42.3% | +0012172214634 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_postal_code` | VARCHAR | 42.3% | 00-815 |
| `employer_poc_postal_code` | VARCHAR | 42.3% | 00-815 |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_state` | VARCHAR | 42.3% | AK |
| `employer_poc_state` | VARCHAR | 42.3% | AK |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 83.2% | "N/A" |
| `employer_province` | VARCHAR | 83.2% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_state` | VARCHAR | 0.0% | AK |
| `end_date` | DATE | 0.0% | 2010-08-10 |
| `end_date` | DATE | 0.0% | 2010-08-10 |
| `full_time_position` | VARCHAR | 8.5% | N |
| `full_time_position` | VARCHAR | 8.5% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `lawfirm_business_fein` | VARCHAR | 89.8% | 01-0000000 |
| `lawfirm_business_fein` | VARCHAR | 89.8% | 01-0000000 |
| `lawfirm_name_business_name` | VARCHAR | 51.9% | (201)489-1351 |
| `lawfirm_name_business_name` | VARCHAR | 51.9% | (201)489-1351 |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `name_of_highest_state_court` | VARCHAR | 52.1% | 	CA Supreme Court |
| `name_of_highest_state_court` | VARCHAR | 52.1% | 	CA Supreme Court |
| `new_concurrent_emp` | VARCHAR | 91.4% | 0 |
| `new_concurrent_emp` | VARCHAR | 91.4% | 0 |
| `new_concurrent_employment` | INTEGER | 25.3% | 0 |
| `new_concurrent_employment` | INTEGER | 25.3% | 0 |
| `new_employment` | INTEGER | 16.7% | 0 |
| `new_employment` | INTEGER | 16.7% | 0 |
| `original_cert_date` | DATE | 94.5% | 2009-07-29 |
| `original_cert_date` | DATE | 94.5% | 2009-07-29 |
| `preparer_business_name` | VARCHAR | 70.4% | (678) 553-7349 |
| `preparer_business_name` | VARCHAR | 70.4% | (678) 553-7349 |
| `preparer_email` | VARCHAR | 70.3% | 	juan.mata@balglobal.com |
| `preparer_email` | VARCHAR | 70.3% | 	juan.mata@balglobal.com |
| `preparer_first_name` | VARCHAR | 70.4% | 	Kiranmai |
| `preparer_first_name` | VARCHAR | 70.4% | 	Kiranmai |
| `preparer_last_name` | VARCHAR | 70.4% | 	Pittakadapala |
| `preparer_last_name` | VARCHAR | 70.4% | 	Pittakadapala |
| `preparer_middle_initial` | VARCHAR | 87.2% | $ |
| `preparer_middle_initial` | VARCHAR | 87.2% | $ |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `public_disclosure` | VARCHAR | 34.0% | BOTH |
| `public_disclosure` | VARCHAR | 34.0% | BOTH |
| `pw_oes_year` | INTEGER | 98.9% | 1 |
| `pw_oes_year` | INTEGER | 98.9% | 1 |
| `pw_other_source` | VARCHAR | 95.0% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_source` | VARCHAR | 95.0% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_survey_name` | VARCHAR | 96.5% | 	Radford Global Technology Survey |
| `pw_survey_name` | VARCHAR | 96.5% | 	Radford Global Technology Survey |
| `pw_survey_publisher` | VARCHAR | 96.4% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_survey_publisher` | VARCHAR | 96.4% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_wage_level` | VARCHAR | 16.2% | I |
| `pw_wage_level` | VARCHAR | 16.2% | I |
| `pw_wage_source` | VARCHAR | 66.5% | CBA |
| `pw_wage_source` | VARCHAR | 66.5% | CBA |
| `pw_wage_source_other` | VARCHAR | 66.7% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_other` | VARCHAR | 66.7% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_year` | INTEGER | 66.5% | 0 |
| `pw_wage_source_year` | INTEGER | 66.5% | 0 |
| `received_date` | DATE | 0.0% | 2009-07-28 |
| `received_date` | DATE | 0.0% | 2009-07-28 |
| `secondary_entity` | VARCHAR | 34.6% | N |
| `secondary_entity` | VARCHAR | 34.6% | N |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `state_of_highest_court` | VARCHAR | 52.1% | /COURT OF APPEALS |
| `state_of_highest_court` | VARCHAR | 52.1% | /COURT OF APPEALS |
| `statutory_basis` | VARCHAR | 81.8% | $60,000 or higher annual wage |
| `statutory_basis` | VARCHAR | 81.8% | $60,000 or higher annual wage |
| `support_h1b` | VARCHAR | 23.7% | N |
| `support_h1b` | VARCHAR | 23.7% | N |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worksite_locations` | INTEGER | 42.4% | 1 |
| `total_worksite_locations` | INTEGER | 42.4% | 1 |
| `trade_name_dba` | VARCHAR | 85.4% | 	 |
| `trade_name_dba` | VARCHAR | 85.4% | 	 |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 49.8% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 49.8% | 0.0 |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `willful_violator` | VARCHAR | 2.3% | N |
| `willful_violator` | VARCHAR | 2.3% | N |
| `worksite_address1` | VARCHAR | 34.0% | 		1960 Ivy Creek Blvd |
| `worksite_address1` | VARCHAR | 34.0% | 		1960 Ivy Creek Blvd |
| `worksite_address2` | VARCHAR | 79.9% | 	 |
| `worksite_address2` | VARCHAR | 79.9% | 	 |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_county` | VARCHAR | 1.3% | #47644 OAKLAND MACOMB |
| `worksite_county` | VARCHAR | 1.3% | #47644 OAKLAND MACOMB |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_workers` | INTEGER | 34.8% | 1 |
| `worksite_workers` | INTEGER | 34.8% | 1 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 42.3% | Q1 |
| `quarter` | VARCHAR | 42.3% | Q1 |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |
| `is_latest` | BOOLEAN | 0.0% | false |

## perm

PERM permanent labor certification applications, one row per application per disclosure file, FY2015-present. 1,391,471 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_city` | VARCHAR | 8.8% | 	 Charlotte |
| `agent_attorney_city` | VARCHAR | 8.8% | 	 Charlotte |
| `agent_attorney_firm_name` | VARCHAR | 10.1% | - N/A |
| `agent_attorney_firm_name` | VARCHAR | 10.1% | - N/A |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `class_of_admission` | VARCHAR | 30.6% | A-3 |
| `class_of_admission` | VARCHAR | 30.6% | A-3 |
| `combination_occupation` | VARCHAR | 62.9% | N |
| `combination_occupation` | VARCHAR | 62.9% | N |
| `country_of_citizenship` | VARCHAR | 24.5% | AFGHANISTAN |
| `country_of_citizenship` | VARCHAR | 24.5% | AFGHANISTAN |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address2` | VARCHAR | 64.8% | 	STE  100 |
| `employer_address2` | VARCHAR | 64.8% | 	STE  100 |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_fein` | VARCHAR | 68.9% | 01-0026590 |
| `employer_fein` | VARCHAR | 68.9% | 01-0026590 |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_num_employees` | INTEGER | 0.0% | 0 |
| `employer_num_employees` | INTEGER | 0.0% | 0 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 96.2% | "N/A" |
| `employer_province` | VARCHAR | 96.2% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_trade_name` | VARCHAR | 91.9% | !melk |
| `employer_trade_name` | VARCHAR | 91.9% | !melk |
| `employer_year_established` | INTEGER | 23.0% | 0 |
| `employer_year_established` | INTEGER | 23.0% | 0 |
| `foreign_worker_birth_country` | VARCHAR | 24.5% | AFGHANISTAN |
| `foreign_worker_birth_country` | VARCHAR | 24.5% | AFGHANISTAN |
| `foreign_worker_curr_employed` | VARCHAR | 63.0% | N |
| `foreign_worker_curr_employed` | VARCHAR | 63.0% | N |
| `foreign_worker_education` | VARCHAR | 24.5% | Associate's |
| `foreign_worker_education` | VARCHAR | 24.5% | Associate's |
| `foreign_worker_education_other` | VARCHAR | 97.2% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_education_other` | VARCHAR | 97.2% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_exp_with_empl` | VARCHAR | 63.0% | N |
| `foreign_worker_exp_with_empl` | VARCHAR | 63.0% | N |
| `foreign_worker_inst_of_ed` | VARCHAR | 33.1% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_inst_of_ed` | VARCHAR | 33.1% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_major` | VARCHAR | 33.3% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_major` | VARCHAR | 33.3% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_req_experience` | VARCHAR | 24.5% | A |
| `foreign_worker_req_experience` | VARCHAR | 24.5% | A |
| `foreign_worker_yrs_ed_comp` | INTEGER | 33.2% | 0 |
| `foreign_worker_yrs_ed_comp` | INTEGER | 33.2% | 0 |
| `is_multiple_locations` | VARCHAR | 75.5% | N |
| `is_multiple_locations` | VARCHAR | 75.5% | N |
| `job_education_min_other` | VARCHAR | 97.8% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_education_min_other` | VARCHAR | 97.8% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `major_field_of_study` | VARCHAR | 36.0% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quo... |
| `major_field_of_study` | VARCHAR | 36.0% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quo... |
| `minimum_education` | VARCHAR | 24.5% | Associate's |
| `minimum_education` | VARCHAR | 24.5% | Associate's |
| `naics_code` | VARCHAR | 38.5% | -3133 |
| `naics_code` | VARCHAR | 38.5% | -3133 |
| `occupation_type` | VARCHAR | 75.5% | College/University Teacher |
| `occupation_type` | VARCHAR | 75.5% | College/University Teacher |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_file_date` | DATE | 99.9% | 1992-04-14 |
| `orig_file_date` | DATE | 99.9% | 1992-04-14 |
| `professional_occupation` | VARCHAR | 62.9% | N |
| `professional_occupation` | VARCHAR | 62.9% | N |
| `pw_determination_date` | DATE | 24.6% | 0014-07-15 |
| `pw_determination_date` | DATE | 24.6% | 0014-07-15 |
| `pw_expiration_date` | DATE | 24.6% | 0214-06-30 |
| `pw_expiration_date` | DATE | 24.6% | 0214-06-30 |
| `pw_level` | VARCHAR | 29.1% | I |
| `pw_level` | VARCHAR | 29.1% | I |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_unit_of_pay` | VARCHAR | 24.6% | Bi-Weekly |
| `pw_unit_of_pay` | VARCHAR | 24.6% | Bi-Weekly |
| `pw_wage` | DOUBLE | 24.5% | 0.0 |
| `pw_wage` | DOUBLE | 24.5% | 0.0 |
| `pw_wage_source` | VARCHAR | 24.5% | CBA |
| `pw_wage_source` | VARCHAR | 24.5% | CBA |
| `pw_wage_source_other` | VARCHAR | 95.7% | &quot;OES&quot; |
| `pw_wage_source_other` | VARCHAR | 95.7% | &quot;OES&quot; |
| `received_date` | DATE | 0.0% | 2005-09-23 |
| `received_date` | DATE | 0.0% | 2005-09-23 |
| `refile` | VARCHAR | 40.3% | N |
| `refile` | VARCHAR | 40.3% | N |
| `required_experience` | VARCHAR | 24.5% | N |
| `required_experience` | VARCHAR | 24.5% | N |
| `required_experience_months` | INTEGER | 58.1% | 0 |
| `required_experience_months` | INTEGER | 58.1% | 0 |
| `required_training` | VARCHAR | 24.5% | N |
| `required_training` | VARCHAR | 24.5% | N |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `schd_a_sheepherder` | VARCHAR | 24.5% | N |
| `schd_a_sheepherder` | VARCHAR | 24.5% | N |
| `soc_code` | VARCHAR | 1.7% | 11-1011 |
| `soc_code` | VARCHAR | 1.7% | 11-1011 |
| `soc_title` | VARCHAR | 1.7% | ,Maintenance Workers, Machinery |
| `soc_title` | VARCHAR | 1.7% | ,Maintenance Workers, Machinery |
| `us_workers_considered` | VARCHAR | 97.7% | N |
| `us_workers_considered` | VARCHAR | 97.7% | N |
| `wage_offer_from` | DOUBLE | 7.4% | 0.0 |
| `wage_offer_from` | DOUBLE | 7.4% | 0.0 |
| `wage_offer_to` | DOUBLE | 63.5% | 0.0 |
| `wage_offer_to` | DOUBLE | 63.5% | 0.0 |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `worksite_address1` | VARCHAR | 38.5% | 	6500  River Place Blvd., Bldg 7 |
| `worksite_address1` | VARCHAR | 38.5% | 	6500  River Place Blvd., Bldg 7 |
| `worksite_address2` | VARCHAR | 75.4% | 	 STE  1003 |
| `worksite_address2` | VARCHAR | 75.4% | 	 STE  1003 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_county` | VARCHAR | 87.7% | 19107 |
| `worksite_county` | VARCHAR | 87.7% | 19107 |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_state` | VARCHAR | 1.0% | AK |
| `worksite_state` | VARCHAR | 1.0% | AK |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 53.0% | Q4 |
| `quarter` | VARCHAR | 53.0% | Q4 |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |
| `is_latest` | BOOLEAN | 0.0% | false |
| `agent_attorney_city` | VARCHAR | 8.8% | 	 Charlotte |
| `agent_attorney_city` | VARCHAR | 8.8% | 	 Charlotte |
| `agent_attorney_firm_name` | VARCHAR | 10.1% | - N/A |
| `agent_attorney_firm_name` | VARCHAR | 10.1% | - N/A |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `class_of_admission` | VARCHAR | 30.6% | A-3 |
| `class_of_admission` | VARCHAR | 30.6% | A-3 |
| `combination_occupation` | VARCHAR | 62.9% | N |
| `combination_occupation` | VARCHAR | 62.9% | N |
| `country_of_citizenship` | VARCHAR | 24.5% | AFGHANISTAN |
| `country_of_citizenship` | VARCHAR | 24.5% | AFGHANISTAN |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address2` | VARCHAR | 64.8% | 	STE  100 |
| `employer_address2` | VARCHAR | 64.8% | 	STE  100 |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_fein` | VARCHAR | 68.9% | 01-0026590 |
| `employer_fein` | VARCHAR | 68.9% | 01-0026590 |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_num_employees` | INTEGER | 0.0% | 0 |
| `employer_num_employees` | INTEGER | 0.0% | 0 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 96.2% | "N/A" |
| `employer_province` | VARCHAR | 96.2% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_trade_name` | VARCHAR | 91.9% | !melk |
| `employer_trade_name` | VARCHAR | 91.9% | !melk |
| `employer_year_established` | INTEGER | 23.0% | 0 |
| `employer_year_established` | INTEGER | 23.0% | 0 |
| `foreign_worker_birth_country` | VARCHAR | 24.5% | AFGHANISTAN |
| `foreign_worker_birth_country` | VARCHAR | 24.5% | AFGHANISTAN |
| `foreign_worker_curr_employed` | VARCHAR | 63.0% | N |
| `foreign_worker_curr_employed` | VARCHAR | 63.0% | N |
| `foreign_worker_education` | VARCHAR | 24.5% | Associate's |
| `foreign_worker_education` | VARCHAR | 24.5% | Associate's |
| `foreign_worker_education_other` | VARCHAR | 97.2% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_education_other` | VARCHAR | 97.2% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_exp_with_empl` | VARCHAR | 63.0% | N |
| `foreign_worker_exp_with_empl` | VARCHAR | 63.0% | N |
| `foreign_worker_inst_of_ed` | VARCHAR | 33.1% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_inst_of_ed` | VARCHAR | 33.1% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_major` | VARCHAR | 33.3% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_major` | VARCHAR | 33.3% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_req_experience` | VARCHAR | 24.5% | A |
| `foreign_worker_req_experience` | VARCHAR | 24.5% | A |
| `foreign_worker_yrs_ed_comp` | INTEGER | 33.2% | 0 |
| `foreign_worker_yrs_ed_comp` | INTEGER | 33.2% | 0 |
| `is_multiple_locations` | VARCHAR | 75.5% | N |
| `is_multiple_locations` | VARCHAR | 75.5% | N |
| `job_education_min_other` | VARCHAR | 97.8% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_education_min_other` | VARCHAR | 97.8% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `major_field_of_study` | VARCHAR | 36.0% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quo... |
| `major_field_of_study` | VARCHAR | 36.0% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quo... |
| `minimum_education` | VARCHAR | 24.5% | Associate's |
| `minimum_education` | VARCHAR | 24.5% | Associate's |
| `naics_code` | VARCHAR | 38.5% | -3133 |
| `naics_code` | VARCHAR | 38.5% | -3133 |
| `occupation_type` | VARCHAR | 75.5% | College/University Teacher |
| `occupation_type` | VARCHAR | 75.5% | College/University Teacher |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_file_date` | DATE | 99.9% | 1992-04-14 |
| `orig_file_date` | DATE | 99.9% | 1992-04-14 |
| `professional_occupation` | VARCHAR | 62.9% | N |
| `professional_occupation` | VARCHAR | 62.9% | N |
| `pw_determination_date` | DATE | 24.6% | 0014-07-15 |
| `pw_determination_date` | DATE | 24.6% | 0014-07-15 |
| `pw_expiration_date` | DATE | 24.6% | 0214-06-30 |
| `pw_expiration_date` | DATE | 24.6% | 0214-06-30 |
| `pw_level` | VARCHAR | 29.1% | I |
| `pw_level` | VARCHAR | 29.1% | I |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_unit_of_pay` | VARCHAR | 24.6% | Bi-Weekly |
| `pw_unit_of_pay` | VARCHAR | 24.6% | Bi-Weekly |
| `pw_wage` | DOUBLE | 24.5% | 0.0 |
| `pw_wage` | DOUBLE | 24.5% | 0.0 |
| `pw_wage_source` | VARCHAR | 24.5% | CBA |
| `pw_wage_source` | VARCHAR | 24.5% | CBA |
| `pw_wage_source_other` | VARCHAR | 95.7% | &quot;OES&quot; |
| `pw_wage_source_other` | VARCHAR | 95.7% | &quot;OES&quot; |
| `received_date` | DATE | 0.0% | 2005-09-23 |
| `received_date` | DATE | 0.0% | 2005-09-23 |
| `refile` | VARCHAR | 40.3% | N |
| `refile` | VARCHAR | 40.3% | N |
| `required_experience` | VARCHAR | 24.5% | N |
| `required_experience` | VARCHAR | 24.5% | N |
| `required_experience_months` | INTEGER | 58.1% | 0 |
| `required_experience_months` | INTEGER | 58.1% | 0 |
| `required_training` | VARCHAR | 24.5% | N |
| `required_training` | VARCHAR | 24.5% | N |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `schd_a_sheepherder` | VARCHAR | 24.5% | N |
| `schd_a_sheepherder` | VARCHAR | 24.5% | N |
| `soc_code` | VARCHAR | 1.7% | 11-1011 |
| `soc_code` | VARCHAR | 1.7% | 11-1011 |
| `soc_title` | VARCHAR | 1.7% | ,Maintenance Workers, Machinery |
| `soc_title` | VARCHAR | 1.7% | ,Maintenance Workers, Machinery |
| `us_workers_considered` | VARCHAR | 97.7% | N |
| `us_workers_considered` | VARCHAR | 97.7% | N |
| `wage_offer_from` | DOUBLE | 7.4% | 0.0 |
| `wage_offer_from` | DOUBLE | 7.4% | 0.0 |
| `wage_offer_to` | DOUBLE | 63.5% | 0.0 |
| `wage_offer_to` | DOUBLE | 63.5% | 0.0 |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `worksite_address1` | VARCHAR | 38.5% | 	6500  River Place Blvd., Bldg 7 |
| `worksite_address1` | VARCHAR | 38.5% | 	6500  River Place Blvd., Bldg 7 |
| `worksite_address2` | VARCHAR | 75.4% | 	 STE  1003 |
| `worksite_address2` | VARCHAR | 75.4% | 	 STE  1003 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_county` | VARCHAR | 87.7% | 19107 |
| `worksite_county` | VARCHAR | 87.7% | 19107 |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_state` | VARCHAR | 1.0% | AK |
| `worksite_state` | VARCHAR | 1.0% | AK |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 53.0% | Q4 |
| `quarter` | VARCHAR | 53.0% | Q4 |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |
| `is_latest` | BOOLEAN | 0.0% | false |

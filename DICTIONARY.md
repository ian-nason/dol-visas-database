# dol-visas Data Dictionary

Built from DOL OFLC quarterly disclosure files (https://www.dol.gov/agencies/eta/foreign-labor/performance).
Column availability varies by fiscal-year era; see crosswalk_lca.csv and crosswalk_perm.csv in the build repo for the exact per-era source-column mappings and every documented drop.

## lca

H-1B/H-1B1/E-3 Labor Condition Applications, one row per application per disclosure file, FY2015-present. 7,479,697 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_address1` | VARCHAR | 52.4% | 	1400 Broadway |
| `agent_attorney_address2` | VARCHAR | 62.7% | 	STE 102 |
| `agent_attorney_city` | VARCHAR | 30.8% | ,Croton |
| `agent_attorney_country` | VARCHAR | 52.4% | AFGHANISTAN |
| `agent_attorney_email_address` | VARCHAR | 58.3% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_first_name` | VARCHAR | 58.3% | (Rachel) Ji-Young |
| `agent_attorney_last_name` | VARCHAR | 58.3% | (Swett) Smith |
| `agent_attorney_middle_name` | VARCHAR | 76.6% | & |
| `agent_attorney_name` | VARCHAR | 69.0% | (DAVID) LIHWEI LIN |
| `agent_attorney_phone` | VARCHAR | 52.4% | +10013236534514 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 52.4% | 0 |
| `agent_attorney_province` | VARCHAR | 93.7% | (213) 384-1900 |
| `agent_attorney_state` | VARCHAR | 33.2% | AK |
| `agent_representing_employer` | VARCHAR | 18.6% | N |
| `agree_to_lc_statement` | VARCHAR | 36.5% | N |
| `amended_petition` | INTEGER | 16.9% | 0 |
| `appendix_a_attached` | VARCHAR | 43.1% | N/A |
| `begin_date` | DATE | 0.0% | 2008-04-09 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `change_employer` | INTEGER | 16.9% | 0 |
| `change_previous_employment` | INTEGER | 16.9% | 0 |
| `continued_employment` | INTEGER | 16.9% | 0 |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address2` | VARCHAR | 61.7% | 					 |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_country` | VARCHAR | 1.7% | AFGHANISTAN |
| `employer_fein` | VARCHAR | 78.7% | 01-0020240 |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_phone` | VARCHAR | 1.7% | (516363587 |
| `employer_phone_ext` | VARCHAR | 94.1% | (716) 8 |
| `employer_poc_address1` | VARCHAR | 49.4% | 	  600 Harrison Street |
| `employer_poc_address2` | VARCHAR | 75.0% | 	 |
| `employer_poc_address_1` | VARCHAR | 93.5% | 	1000  ASU Drive |
| `employer_poc_address_2` | VARCHAR | 96.6% | 	 |
| `employer_poc_city` | VARCHAR | 42.9% | 	 Jersey City |
| `employer_poc_country` | VARCHAR | 42.9% | AFGHANISTAN |
| `employer_poc_email` | VARCHAR | 42.9% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_first_name` | VARCHAR | 42.9% | 	 Belinda |
| `employer_poc_job_title` | VARCHAR | 42.9% | 	$151154.00 |
| `employer_poc_last_name` | VARCHAR | 42.9% | 	Arnaudez |
| `employer_poc_middle_name` | VARCHAR | 84.4% | 	 |
| `employer_poc_phone` | VARCHAR | 42.9% | +0012172214634 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_postal_code` | VARCHAR | 42.9% | 00-815 |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_state` | VARCHAR | 43.0% | AK |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 83.1% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `end_date` | DATE | 0.0% | 2010-08-10 |
| `full_time_position` | VARCHAR | 8.7% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `lawfirm_business_fein` | VARCHAR | 90.8% | 01-0000000 |
| `lawfirm_name_business_name` | VARCHAR | 52.3% | (201)489-1351 |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `name_of_highest_state_court` | VARCHAR | 52.5% | 	CA Supreme Court |
| `new_concurrent_emp` | VARCHAR | 91.3% | 0 |
| `new_concurrent_employment` | INTEGER | 25.7% | 0 |
| `new_employment` | INTEGER | 16.9% | 0 |
| `original_cert_date` | DATE | 94.6% | 2009-07-29 |
| `preparer_business_name` | VARCHAR | 70.7% | (678) 553-7349 |
| `preparer_email` | VARCHAR | 70.6% | 	juan.mata@balglobal.com |
| `preparer_first_name` | VARCHAR | 70.7% | 	Kiranmai |
| `preparer_last_name` | VARCHAR | 70.7% | 	Pittakadapala |
| `preparer_middle_initial` | VARCHAR | 87.2% | $ |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `public_disclosure` | VARCHAR | 34.5% | BOTH |
| `pw_oes_year` | INTEGER | 98.8% | 1 |
| `pw_other_source` | VARCHAR | 95.1% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_survey_name` | VARCHAR | 96.5% | 	Radford Global Technology Survey |
| `pw_survey_publisher` | VARCHAR | 96.5% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_wage_level` | VARCHAR | 16.2% | I |
| `pw_wage_source` | VARCHAR | 66.0% | CBA |
| `pw_wage_source_other` | VARCHAR | 66.2% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_year` | INTEGER | 66.0% | 0 |
| `received_date` | DATE | 0.0% | 2009-07-28 |
| `secondary_entity` | VARCHAR | 35.2% | N |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `state_of_highest_court` | VARCHAR | 52.5% | /COURT OF APPEALS |
| `statutory_basis` | VARCHAR | 81.9% | $60,000 or higher annual wage |
| `support_h1b` | VARCHAR | 24.0% | N |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worksite_locations` | INTEGER | 43.1% | 1 |
| `trade_name_dba` | VARCHAR | 85.3% | 	 |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 49.5% | 0.0 |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `willful_violator` | VARCHAR | 2.3% | N |
| `worksite_address1` | VARCHAR | 34.5% | 		1960 Ivy Creek Blvd |
| `worksite_address2` | VARCHAR | 80.0% | 	 |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_county` | VARCHAR | 1.3% | #47644 OAKLAND MACOMB |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_workers` | INTEGER | 35.3% | 1 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 42.9% | Q1 |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |

## perm

PERM permanent labor certification applications, one row per application per disclosure file, FY2015-present. 1,332,942 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_city` | VARCHAR | 8.9% | 	 Charlotte |
| `agent_attorney_firm_name` | VARCHAR | 10.3% | - N/A |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `class_of_admission` | VARCHAR | 27.6% | A-3 |
| `combination_occupation` | VARCHAR | 61.3% | N |
| `country_of_citizenship` | VARCHAR | 21.2% | AFGHANISTAN |
| `decision_date` | DATE | 0.0% | 2014-10-01 |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address2` | VARCHAR | 65.2% | 	STE  100 |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_fein` | VARCHAR | 71.9% | 01-0026590 |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_num_employees` | INTEGER | 0.1% | 0 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 96.7% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_trade_name` | VARCHAR | 92.9% | !melk |
| `employer_year_established` | INTEGER | 24.0% | 0 |
| `foreign_worker_birth_country` | VARCHAR | 21.2% | AFGHANISTAN |
| `foreign_worker_curr_employed` | VARCHAR | 61.3% | N |
| `foreign_worker_education` | VARCHAR | 21.2% | Associate's |
| `foreign_worker_education_other` | VARCHAR | 97.1% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_exp_with_empl` | VARCHAR | 61.3% | N |
| `foreign_worker_inst_of_ed` | VARCHAR | 30.1% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_major` | VARCHAR | 30.4% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_req_experience` | VARCHAR | 21.2% | A |
| `foreign_worker_yrs_ed_comp` | INTEGER | 30.2% | 0 |
| `is_multiple_locations` | VARCHAR | 78.9% | N |
| `job_education_min_other` | VARCHAR | 97.7% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `major_field_of_study` | VARCHAR | 33.2% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quo... |
| `minimum_education` | VARCHAR | 21.2% | Associate's |
| `naics_code` | VARCHAR | 40.2% | -3133 |
| `occupation_type` | VARCHAR | 78.9% | College/University Teacher |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_file_date` | DATE | 99.9% | 1992-04-14 |
| `professional_occupation` | VARCHAR | 61.3% | N |
| `pw_determination_date` | DATE | 21.2% | 0014-07-15 |
| `pw_expiration_date` | DATE | 21.3% | 0214-06-30 |
| `pw_level` | VARCHAR | 25.9% | I |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_unit_of_pay` | VARCHAR | 21.3% | Bi-Weekly |
| `pw_wage` | DOUBLE | 21.2% | 0.0 |
| `pw_wage_source` | VARCHAR | 21.2% | CBA |
| `pw_wage_source_other` | VARCHAR | 95.5% | &quot;OES&quot; |
| `received_date` | DATE | 0.0% | 2005-09-23 |
| `refile` | VARCHAR | 37.7% | N |
| `required_experience` | VARCHAR | 21.2% | N |
| `required_experience_months` | INTEGER | 56.2% | 0 |
| `required_training` | VARCHAR | 21.2% | N |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `schd_a_sheepherder` | VARCHAR | 21.2% | N |
| `soc_code` | VARCHAR | 1.8% | 11-1011 |
| `soc_title` | VARCHAR | 1.8% | ,Maintenance Workers, Machinery |
| `us_workers_considered` | VARCHAR | 97.6% | N |
| `wage_offer_from` | DOUBLE | 7.7% | 0.0 |
| `wage_offer_to` | DOUBLE | 64.3% | 0.0 |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `worksite_address1` | VARCHAR | 40.2% | 	6500  River Place Blvd., Bldg 7 |
| `worksite_address2` | VARCHAR | 76.2% | 	 STE  1003 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_county` | VARCHAR | 91.6% | ABINGTON |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_state` | VARCHAR | 0.9% | AK |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 55.3% | Q3 |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |

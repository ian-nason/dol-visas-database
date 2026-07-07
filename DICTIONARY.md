# dol-visas Data Dictionary

Built from DOL OFLC quarterly disclosure files (https://www.dol.gov/agencies/eta/foreign-labor/performance).
Column availability varies by fiscal-year era; see crosswalk_lca.csv and crosswalk_perm.csv in the build repo for the exact per-era source-column mappings and every documented drop.

## lca

H-1B/H-1B1/E-3 Labor Condition Applications, one row per application per disclosure file, FY2015-present. 7,252,588 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_address1` | VARCHAR | 53.2% | 	1400 Broadway |
| `agent_attorney_address2` | VARCHAR | 63.3% | 	STE 102 |
| `agent_attorney_city` | VARCHAR | 31.0% | ,Croton |
| `agent_attorney_country` | VARCHAR | 53.2% | AFGHANISTAN |
| `agent_attorney_email_address` | VARCHAR | 59.4% | 	Dana.Singleton@ogletreedeakins.com |
| `agent_attorney_first_name` | VARCHAR | 59.4% | (Rachel) Ji-Young |
| `agent_attorney_last_name` | VARCHAR | 59.4% | (Swett) Smith |
| `agent_attorney_middle_name` | VARCHAR | 77.0% | & |
| `agent_attorney_name` | VARCHAR | 68.0% | (DAVID) LIHWEI LIN |
| `agent_attorney_phone` | VARCHAR | 53.2% | +10013236534514 |
| `agent_attorney_phone_ext` | VARCHAR | 96.7% | 0 |
| `agent_attorney_postal_code` | VARCHAR | 53.2% | 0 |
| `agent_attorney_province` | VARCHAR | 93.8% | (213) 384-1900 |
| `agent_attorney_state` | VARCHAR | 33.4% | AK |
| `agent_representing_employer` | VARCHAR | 19.2% | N |
| `agree_to_lc_statement` | VARCHAR | 37.6% | N |
| `amended_petition` | INTEGER | 17.5% | 0 |
| `appendix_a_attached` | VARCHAR | 44.4% | N/A |
| `begin_date` | DATE | 90.8% | 2010-06-07 |
| `case_number` | VARCHAR | 0.0% | I-200-09121-701936 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `change_employer` | INTEGER | 17.5% | 0 |
| `change_previous_employment` | INTEGER | 17.5% | 0 |
| `continued_employment` | INTEGER | 17.5% | 0 |
| `decision_date` | DATE | 100.0% |  |
| `employer_address1` | VARCHAR | 0.0% | 	  225 West Wacker Drive |
| `employer_address2` | VARCHAR | 61.9% | 					 |
| `employer_city` | VARCHAR | 0.0% | 	  Palo Alto |
| `employer_country` | VARCHAR | 1.7% | AFGHANISTAN |
| `employer_fein` | VARCHAR | 81.1% | 01-0020240 |
| `employer_name` | VARCHAR | 0.0% | 	1. UBS BUSINESS SOLUTIONS US LLC |
| `employer_phone` | VARCHAR | 1.7% | (516363587 |
| `employer_phone_ext` | VARCHAR | 94.0% | (716) 8 |
| `employer_poc_address1` | VARCHAR | 51.0% | 	  600 Harrison Street |
| `employer_poc_address2` | VARCHAR | 75.8% | 	 |
| `employer_poc_address_1` | VARCHAR | 93.3% | 	1000  ASU Drive |
| `employer_poc_address_2` | VARCHAR | 96.5% | 	 |
| `employer_poc_city` | VARCHAR | 44.3% | 	 Jersey City |
| `employer_poc_country` | VARCHAR | 44.3% | AFGHANISTAN |
| `employer_poc_email` | VARCHAR | 44.3% | 	 ntroubh@badgerandwinters.com |
| `employer_poc_first_name` | VARCHAR | 44.3% | 	 Belinda |
| `employer_poc_job_title` | VARCHAR | 44.3% | 	$151154.00 |
| `employer_poc_last_name` | VARCHAR | 44.3% | 	Arnaudez |
| `employer_poc_middle_name` | VARCHAR | 84.5% | 	 |
| `employer_poc_phone` | VARCHAR | 44.3% | +0012172214634 |
| `employer_poc_phone_ext` | VARCHAR | 96.7% | 0 |
| `employer_poc_postal_code` | VARCHAR | 44.3% | 0000 |
| `employer_poc_province` | VARCHAR | 99.6% | "N/A" |
| `employer_poc_state` | VARCHAR | 44.3% | AK |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 82.7% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `end_date` | DATE | 90.8% | 2010-08-10 |
| `full_time_position` | VARCHAR | 8.9% | N |
| `h_1b_dependent` | VARCHAR | 2.3% | N |
| `job_title` | VARCHAR | 0.0% | 	  Product Management Associate |
| `lawfirm_business_fein` | VARCHAR | 92.9% | 01-0176171 |
| `lawfirm_name_business_name` | VARCHAR | 53.2% | (201)489-1351 |
| `masters_exemption` | VARCHAR | 100.0% | N |
| `naics_code` | VARCHAR | 0.0% | &NBSP; |
| `name_of_highest_state_court` | VARCHAR | 53.3% | 	CA Supreme Court |
| `new_concurrent_emp` | VARCHAR | 91.0% | 0 |
| `new_concurrent_employment` | INTEGER | 26.5% | 0 |
| `new_employment` | INTEGER | 17.5% | 0 |
| `original_cert_date` | DATE | 100.0% |  |
| `preparer_business_name` | VARCHAR | 71.4% | (678) 553-7349 |
| `preparer_email` | VARCHAR | 71.3% | 	juan.mata@balglobal.com |
| `preparer_first_name` | VARCHAR | 71.4% | 	Kiranmai |
| `preparer_last_name` | VARCHAR | 71.4% | 	Pittakadapala |
| `preparer_middle_initial` | VARCHAR | 87.3% | $ |
| `prevailing_wage` | DOUBLE | 0.5% | 0.0 |
| `public_disclosure` | VARCHAR | 35.6% | BOTH |
| `pw_oes_year` | INTEGER | 98.8% | 1 |
| `pw_other_source` | VARCHAR | 95.2% | &QUOT;OFLC ONLINE DATA CENTER&QUOT; |
| `pw_other_year` | INTEGER | 88.8% | 1 |
| `pw_survey_name` | VARCHAR | 96.7% | 	Radford Global Technology Survey |
| `pw_survey_publisher` | VARCHAR | 96.6% | "Willis Tower Watson: Mid Mngt Pro & Supp Comp Survey" |
| `pw_tracking_number` | VARCHAR | 99.2% | 'N/A' |
| `pw_unit_of_pay` | VARCHAR | 0.5% | Bi-Weekly |
| `pw_wage_level` | VARCHAR | 16.5% | I |
| `pw_wage_source` | VARCHAR | 64.9% | CBA |
| `pw_wage_source_other` | VARCHAR | 65.1% | " OFLC ONLINE DATA CENTER" |
| `pw_wage_source_year` | INTEGER | 64.9% | 0 |
| `received_date` | DATE | 100.0% |  |
| `secondary_entity` | VARCHAR | 36.3% | N |
| `secondary_entity_business_name` | VARCHAR | 83.1% | 	 AMD Inc |
| `soc_code` | VARCHAR | 0.0% | 030 |
| `soc_title` | VARCHAR | 0.0% | 11-9121 |
| `state_of_highest_court` | VARCHAR | 53.3% | /COURT OF APPEALS |
| `statutory_basis` | VARCHAR | 81.9% | $60,000 or higher annual wage |
| `support_h1b` | VARCHAR | 24.8% | N |
| `total_worker_positions` | INTEGER | 0.0% | 0 |
| `total_worksite_locations` | INTEGER | 44.4% | 1 |
| `trade_name_dba` | VARCHAR | 85.2% | 	 |
| `visa_class` | VARCHAR | 0.0% | E-3 Australian |
| `wage_rate_of_pay_from` | DOUBLE | 0.0% | 0.0 |
| `wage_rate_of_pay_to` | DOUBLE | 48.8% | 0.0 |
| `wage_unit_of_pay` | VARCHAR | 0.0% | Bi-Weekly |
| `willful_violator` | VARCHAR | 2.3% | N |
| `worksite_address1` | VARCHAR | 35.6% | 		1960 Ivy Creek Blvd |
| `worksite_address2` | VARCHAR | 80.4% | 	 |
| `worksite_city` | VARCHAR | 0.0% | 	 Lansing |
| `worksite_county` | VARCHAR | 4.1% | #47644 OAKLAND MACOMB |
| `worksite_postal_code` | VARCHAR | 0.0% | $48,797 |
| `worksite_state` | VARCHAR | 0.0% | AK |
| `worksite_workers` | INTEGER | 36.4% | 1 |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 44.3% | Q1 |
| `source_file` | VARCHAR | 0.0% | H-1B_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |

## perm

PERM permanent labor certification applications, one row per application per disclosure file, FY2015-present. 1,280,488 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `agent_attorney_city` | VARCHAR | 8.9% | 	 Charlotte |
| `agent_attorney_firm_name` | VARCHAR | 10.4% | - N/A |
| `agent_attorney_state` | VARCHAR | 10.9% | AB |
| `case_number` | VARCHAR | 0.0% | A-05269-36154 |
| `case_status` | VARCHAR | 0.0% | CERTIFIED |
| `class_of_admission` | VARCHAR | 24.6% | A-3 |
| `combination_occupation` | VARCHAR | 59.7% | N |
| `country_of_citizenship` | VARCHAR | 17.9% | AFGHANISTAN |
| `decision_date` | DATE | 100.0% |  |
| `employer_address1` | VARCHAR | 0.0% | 	274 LAKE WALES DR |
| `employer_address2` | VARCHAR | 65.5% | # 1 |
| `employer_city` | VARCHAR | 0.0% | 	 	  BRECKSVILLE |
| `employer_country` | VARCHAR | 0.1% | BRAZIL |
| `employer_fein` | VARCHAR | 74.9% | 01-0026590 |
| `employer_name` | VARCHAR | 0.0% | 	Argos Puerto Rico Corp. |
| `employer_num_employees` | INTEGER | 0.1% | 0 |
| `employer_phone` | VARCHAR | 0.0% | ( 626) 969-9797 |
| `employer_postal_code` | VARCHAR | 0.0% | 0 |
| `employer_province` | VARCHAR | 97.1% | "N/A" |
| `employer_state` | VARCHAR | 0.0% | AK |
| `employer_trade_name` | VARCHAR | 93.9% | !melk |
| `employer_year_established` | INTEGER | 25.0% | 0 |
| `foreign_worker_birth_country` | VARCHAR | 18.0% | AFGHANISTAN |
| `foreign_worker_curr_employed` | VARCHAR | 59.7% | N |
| `foreign_worker_education` | VARCHAR | 18.0% | Associate's |
| `foreign_worker_education_other` | VARCHAR | 97.0% | &QUOT;2 ADDTL YRS REL EXP IN MEETING BACH DEG REQT *SEE SECT H.14*&QUOT; |
| `foreign_worker_exp_with_empl` | VARCHAR | 59.7% | N |
| `foreign_worker_inst_of_ed` | VARCHAR | 27.3% | # 1 HIGH SCHOOL, CHARENTSAVAN, ARMENIA |
| `foreign_worker_major` | VARCHAR | 27.5% | (1) CHEMISTRY AND (2) MGMT FOR STEEL INDUSTRY (RELATED TO JOB/ENGINEERING) |
| `foreign_worker_req_experience` | VARCHAR | 18.0% | A |
| `foreign_worker_yrs_ed_comp` | INTEGER | 27.4% | 0 |
| `is_multiple_locations` | VARCHAR | 82.1% | N |
| `job_education_min_other` | VARCHAR | 97.6% | (7) years or more of Construction and/or Infrared Work Experience |
| `job_title` | VARCHAR | 0.0% | 	CONSTRUCTION PROJECT MANAGER (FRAMING AND OPERATIONS) |
| `layoff_in_past_six_months` | VARCHAR | 0.0% | N |
| `major_field_of_study` | VARCHAR | 30.5% | &quot;Computer Science&quot;, &quot;Information Technology and Management&quot;  |
| `minimum_education` | VARCHAR | 17.9% | Associate's |
| `naics_code` | VARCHAR | 41.8% | -3133 |
| `occupation_type` | VARCHAR | 82.1% | College/University Teacher |
| `orig_case_number` | VARCHAR | 99.9% | #11684973 |
| `orig_file_date` | DATE | 100.0% |  |
| `professional_occupation` | VARCHAR | 59.7% | N |
| `pw_determination_date` | DATE | 92.0% | 0014-07-15 |
| `pw_expiration_date` | DATE | 92.0% | 0214-06-30 |
| `pw_level` | VARCHAR | 22.9% | I |
| `pw_tracking_number` | VARCHAR | 0.4% | *TN ONLY PROVID |
| `pw_unit_of_pay` | VARCHAR | 18.1% | Bi-Weekly |
| `pw_wage` | DOUBLE | 18.0% | 0.0 |
| `pw_wage_source` | VARCHAR | 18.0% | CBA |
| `pw_wage_source_other` | VARCHAR | 95.3% | &quot;OES&quot; |
| `received_date` | DATE | 100.0% |  |
| `refile` | VARCHAR | 35.2% | N |
| `required_experience` | VARCHAR | 18.0% | N |
| `required_experience_months` | INTEGER | 54.4% | 0 |
| `required_training` | VARCHAR | 18.0% | N |
| `required_training_months` | INTEGER | 99.0% | 0 |
| `schd_a_sheepherder` | VARCHAR | 18.0% | N |
| `soc_code` | VARCHAR | 1.9% | 11-1011 |
| `soc_title` | VARCHAR | 1.8% | ,Maintenance Workers, Machinery |
| `us_workers_considered` | VARCHAR | 97.5% | N |
| `wage_offer_from` | DOUBLE | 8.0% | 0.0 |
| `wage_offer_to` | DOUBLE | 64.9% | 0.0 |
| `wage_offer_unit_of_pay` | VARCHAR | 0.1% | Bi-Weekly |
| `worksite_address1` | VARCHAR | 41.8% | #1 DIASTER RIDGE ROAD |
| `worksite_address2` | VARCHAR | 77.0% | 	 STE  1003 |
| `worksite_city` | VARCHAR | 0.0% | (213) 505-4566 |
| `worksite_county` | VARCHAR | 95.3% | ABINGTON |
| `worksite_postal_code` | VARCHAR | 0.0% | * 40511 |
| `worksite_state` | VARCHAR | 0.8% | AK |
| `fiscal_year` | INTEGER | 0.0% | 2015 |
| `quarter` | VARCHAR | 57.6% | Q2 |
| `source_file` | VARCHAR | 0.0% | PERM_Disclosure_Data_FY15_Q4.xlsx |
| `is_latest` | BOOLEAN | 0.0% | false |

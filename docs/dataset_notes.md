# Dataset Notes: Airport Security Checkpoint Data (4TU)

## Overview
- **Source:** 4TU.ResearchData, "Airport Security Checkpoint Data" ( Janssen et al. 2020)
- **Collected at:** Rotterdam The Hague Airport
- **Purpose:** published with the paper "Data-driven Analysis of Airport Security Checkpoint Operations" (Aerospace, 2020)
- **Files in data/raw/:**
 -'README.pdf': description of the dataset
 -'security_checkpoint_data.xlsx': the data
- **Sheets:** one sheet per day ([13] days): [tab names, e.g. 2018_12_18a, etc) 


## 1. Columns and units

| Spreadsheet column | README name | Meaning | Unit | Type |
|---|---|---|---|---|
|Lane Number | Not described | Which security lane the passenger used | None | category
|Date | Date | Day that the passenger was recorded  | dd/mm/yyyy | Date
|Business, Senior, Family, Young, PRM, regular | b, s, f, y, p, r | Each passenger grouping | None | Indicator (yes/no)
|Experience | J | The level of experience that a passenger has | None | Indicator (experienced/not experienced) 
|Time Start Baggage Drop Off | K | The time that the passenger starts to drops their luggage off | Seconds since midnight | Timestamp
|Time Start WTMD 1, 2, 3 | N, O , P | The first, second, and third time that a passenger walks through a metal detector | Seconds since midnight | Timestamp
|Time Start WTMD Check | Q | The starting time that the passenger receives a patdown | Seconds since midnight | Timestamp
|Time End WTMD Check | R | The ending time that the passenger receives a patdown | Seconds since midnight | Timestamp
|Time Start ETD Check | S | The starting time that the passenger receives an explosive trace detection check | Seconds since midnight | Timestamp
|Time End ETD Check | T | The ending time that the passenger receives an explosive trace detection check | Seconds since midnight | Timestamp
|Time Start Baggage reclaim | U | The time the passenger starts to reclaim their luggage | Seconds since midnight | Timestamp
|Time End Baggage Reclaim | V | The time the passenger ends to reclaim their luggage | Seconds since midnight | Timestamp
|Group Size | W | The size of the group that passenger is traveling with | Passengers | Count
|Time Start Baggage Check | X | The starting time that the passenger receives a baggage check | Seconds since midnight | Timestamp
|Time End Baggage Check | Y | The ending time that the passenger receives a baggage check | Seconds since midnight | Timestamp
 

## 2. Arrival times or only durations?

-The data racords timestamps (seconds since midnight) for the start and end times of each stage
-Durations can be calculated by subtraction (end - start)
-**Queue entry time record?** [no]
-First timestamp is at beginning of baggage drop and when service is started, not when the passenger joined the line. Generate arrivals randomly, at a rate estimated from passengers per hour


## 3. Stages and number of passenger

-**Stages, in order:**
 1. Baggage Drop: everyone
 2. Metal Detector Walkthrough 1st, 2nd, 3rd: everyone; some passengers pass through multiple times
 3. Explosive Trace Detection: some people
 4. Baggage Reclaim: everyone
 5. Additional Baggage Check: some people

## 4. Licence and citation

-**Licence** CC by 4.0 (Sharing allowed with credit to the authors)
-**Can I commit the data to Github?** Yes, with the citation in the README file
- **DOI:** 10.4121/uuid:6246e6a6-d149-420f-a6a4-7afd08f154b5
- **Citation:** Janssen, S.; van der Sommen, R.; Dilweg, A.; Sharpanskykh, A. (2020).
  Airport Security Checkpoint Data. Version 1. 4TU.ResearchData. Dataset.
  https://doi.org/10.4121/uuid:6246e6a6-d149-420f-a6a4-7afd08f154b5

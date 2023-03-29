/bin/bash
# This script eill quesry covid data and display it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hostpitalized')
RECOVERED=$(echo $DATA | jq '.[0].recovered')
TOTAL=$(echo $DATA | jq '.[0].total')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive, $NEGATIVE negative,$DEATH death, $HOSPITALIZED hospitalized,
$RECOVERED recovered, $TOTAL total, $DEATHINCREASE deathIncrease, COVID cases"

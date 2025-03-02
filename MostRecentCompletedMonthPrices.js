const data = {
    graph: {
        series: [
            { x: 1706745600, y: '210000' },
            { x: 1722470400, y: '195000' },
            { x: 1680307200, y: '160000' },
            { x: 1698796800, y: '105000' },
            { x: 1717200000, y: '170000' },
            { x: 1648771200, y: '130000' },
            { x: 1688169600, y: '140823.44' },
            { x: 1672531200, y: '135000' },
            { x: 1656633600, y: '120032.89' },
            { x: 1646092800, y: '130000' },
            { x: 1654041600, y: '100000' },
            { x: 1667260800, y: '130000' },
            { x: 1727740800, y: '200000' },
            { x: 1730419200, y: '117500' },
            { x: 1651363200, y: '119000' },
            { x: 1738368000, y: '175000' },
            { x: 1690848000, y: '170000' },
            { x: 1664582400, y: '175000' }
        ]
    }
};

function getMostRecentCompletedMonthPrices(data, currentDate = new Date()) {
    // Convert Unix timestamps to Date objects and sort chronologically
    const sortedEntries = [...data.graph.series]
        .map(entry => ({
            date: new Date(entry.x * 1000),
            price: parseFloat(entry.y)
        }))
        .sort((a, b) => b.date - a.date); // Sort in descending order

    console.log('All dates:', sortedEntries.map(e => e.date.toLocaleDateString()));

    // Find the most recent month with data
    const mostRecentEntry = sortedEntries[0];
    const targetMonth = mostRecentEntry.date.getMonth();
    const targetYear = mostRecentEntry.date.getFullYear();

    console.log(`Most recent month with data: ${new Date(targetYear, targetMonth).toLocaleString('default', { month: 'long' })}, Year: ${targetYear}`);

    // Find prices for the target month/year
    const targetPrices = sortedEntries.filter(entry => 
        entry.date.getMonth() === targetMonth && 
        entry.date.getFullYear() === targetYear
    );

    console.log('Matching prices:', targetPrices.map(p => p.price));

    return {
        month: new Date(targetYear, targetMonth).toLocaleString('default', { month: 'long' }),
        year: targetYear,
        prices: targetPrices.map(entry => entry.price),
        averagePrice: targetPrices.length > 0 ? 
            targetPrices.reduce((sum, entry) => sum + entry.price, 0) / targetPrices.length : null
    };
}

// Example usage with sample date
const sampleDate = new Date('2025-02-11');
console.log('\nFinal Result:');
console.log(getMostRecentCompletedMonthPrices(data, sampleDate));


/*
* Final Result:
* All dates: [
*  '2/1/2025',  '11/1/2024',
*   '10/1/2024', '8/1/2024',
*   '6/1/2024',  '2/1/2024',
*   '11/1/2023', '8/1/2023',
*   '7/1/2023',  '4/1/2023',
*   '1/1/2023',  '11/1/2022',
*   '10/1/2022', '7/1/2022',
*   '6/1/2022',  '5/1/2022',
*   '4/1/2022',  '3/1/2022'
* ]
* Most recent month with data: February, Year: 2025
* Matching prices: [ 175000 ]
* {
*   month: 'February',
*   year: 2025,
*   prices: [ 175000 ],
*   averagePrice: 175000
* }
*/

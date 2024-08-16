import express from "express";

export interface WeatherData {
    latitude: number
    longitude: number
    generationtime_ms: number
    utc_offset_seconds: number
    timezone: string
    timezone_abbreviation: string
    elevation: number
    hourly_units: any
    hourly: any
  }
  
//   export interface HourlyUnits {
//     time: string
//     temperature_2m: string
//   }
  
//   export interface Hourly {
//     time: string[]
//     temperature_2m: number[]
//   }

const app = express();

const port = 3001;

const callApi = async (lat: string, lon: string, from: string, to: string, type: string) => {
    try{
        const response = await fetch(`https://api.open-meteo.com/v1/gfs?end_date=${to}&hourly=${type}&latitude=${lat}&longitude=${lon}&start_date=${from}`);
        const data = await response.json() as WeatherData;
        //console.log(data)
    
        let hourly = [];
    
        for (let i = 0; i < data.hourly.time.length; i++) {
            hourly.push({time: data.hourly.time[i], value: data.hourly[type][i]})
        }
    
        //console.log(hourly);
        return hourly;
    }
    catch (e) {
        console.error("Error in fetching data" + e)
        return []
    }
}

app.get("/", async (req, res) => {
    console.log(req.query.lat)
    console.log(req.query.lon)
    console.log(req.query.from)
    console.log(req.query.to)
    console.log(req.query.type)

    const lat = req.query.lat as string;
    const lon = req.query.lon as string;
    const from = req.query.from as string;
    const to = req.query.to as string;
    const type = req.query.type as string;

    console.log(lat)
    
    // temperature_2m,relative_humidity_2m,rain,cloud_cover,wind_speed_10m

    switch (type) {
        case "temperature":
            const temp_response = await callApi(lat, lon, from, to, "temperature_2m");
            res.send(temp_response);
            break;
        case "humidity":
            const humidity_response = await callApi(lat, lon, from, to, "relative_humidity_2m");
            res.send(humidity_response);
            break;
        case "rain":
            const rain_response = await callApi(lat, lon, from, to, "rain");
            res.send(rain_response);
            break
        case "cloud":
            const cloud_response = await callApi(lat, lon, from, to, "cloud_cover");
            res.send(cloud_response);
            break;
        case "wind":
            const wind_response = await callApi(lat, lon, from, to, "wind_speed_10m");
            res.send(wind_response);
            break;
        default:    
            res.send("Invalid type");
            break;
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
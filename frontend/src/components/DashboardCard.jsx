import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import "../styles/dashboard.css";

import {
    getEmployees,
    getAttendance,
    getApplications,
    getWebsites,
    getFiles,
    getUSB
} from "../api/dashboardApi";

function Dashboard() {

    const [stats, setStats] = useState({
        employees:0,
        attendance:0,
        applications:0,
        websites:0,
        files:0,
        usb:0
    });

    useEffect(()=>{

        async function loadDashboard(){

            try{

                const employees=await getEmployees();
                const attendance=await getAttendance();
                const applications=await getApplications();
                const websites=await getWebsites();
                const files=await getFiles();
                const usb=await getUSB();

                setStats({

                    employees:employees.data.length,

                    attendance:attendance.data.length,

                    applications:applications.data.length,

                    websites:websites.data.length,

                    files:files.data.length,

                    usb:usb.data.length

                });

            }

            catch(err){

                console.log(err);

            }

        }

        loadDashboard();

    },[]);

    return(

        <Layout>

            <h2 className="mb-4">
                Dashboard
            </h2>

            <div className="row g-4">

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>Total Employees</h5>

                        <h1>{stats.employees}</h1>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>Attendance</h5>

                        <h1>{stats.attendance}</h1>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>Applications</h5>

                        <h1>{stats.applications}</h1>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>Websites</h5>

                        <h1>{stats.websites}</h1>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>Files</h5>

                        <h1>{stats.files}</h1>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card shadow p-4">

                        <h5>USB Devices</h5>

                        <h1>{stats.usb}</h1>

                    </div>

                </div>

            </div>

        </Layout>

    );

}

export default Dashboard;
import API from "./api";

export const getEmployees = () => API.get("/employees");

export const getAttendance = () => API.get("/attendance");

export const getActivity = () => API.get("/activity");

export const getApplications = () => API.get("/application");

export const getWebsites = () => API.get("/website");

export const getFiles = () => API.get("/file");

export const getUSB = () => API.get("/usb");
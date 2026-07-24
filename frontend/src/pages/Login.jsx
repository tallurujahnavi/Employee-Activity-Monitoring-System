import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";
import "../styles/login.css";

function Login() {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);

    const login = async (e) => {
        e.preventDefault();

        setLoading(true);

        try {
            const response = await API.post("/auth/admin/login", {
                email,
                password
            });

            console.log("Login Response:", response.data);

            if (response.data.success) {

                // Save JWT Token
                localStorage.setItem("token", response.data.token);

                // Save Admin Details
                localStorage.setItem(
                    "admin",
                    JSON.stringify(response.data.admin)
                );

                alert(response.data.message);

                navigate("/dashboard");

            } else {
                alert(response.data.message);
            }

        } catch (error) {

            console.error(error);

            if (error.response) {
                alert(error.response.data.message);
            } else {
                alert("Unable to connect to backend.");
            }

        }

        setLoading(false);
    };

    return (
        <div className="login-container">

            <div className="login-card">

                <h2>Employee Activity Monitoring System</h2>

                <p>Administrator Login</p>

                <form onSubmit={login}>

                    <input
                        type="email"
                        placeholder="Email Address"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />

                    <button type="submit" disabled={loading}>
                        {loading ? "Logging in..." : "Login"}
                    </button>

                </form>

            </div>

        </div>
    );
}

export default Login;
import { redirect } from "react-router-dom";

export async function RequireAuthService() {
    if (localStorage.getItem("access_token") === null) {
        return redirect("/admin/login");
    }
    return true;
}

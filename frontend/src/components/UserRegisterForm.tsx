import { useState } from "react";
import { useRouter } from "next/router";
import { api } from "@/utils/api";
import axios from "axios";

export default function UserRegistrationForm() {
  const router = useRouter();

  const [formData, setFormData] = useState({
    first_name: "",
    family_name: "",
    email: "",
    phone_number: "",
    password: "",
    company: "",
    country: ""
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post("/users/register", formData);
      router.push("/login"); // Redirect after successful registration
    } catch (error) {
      console.error("Failed to register user:", error);
      if (axios.isAxiosError(error) && error.response) {
        alert("Registration failed: " + error.response.data.detail);
      } else {
        alert("An unexpected error occurred.");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 border rounded shadow space-y-4">
      <h2 className="text-2xl font-bold mb-4">Create your account</h2>

      <input name="first_name" placeholder="First Name" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <input name="family_name" placeholder="Family Name" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <input type="email" name="email" placeholder="Business Email" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <input name="phone_number" placeholder="+1234567890" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <input type="password" name="password" placeholder="Password" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <input name="company" placeholder="Company" required
        className="block w-full p-2 border rounded"
        onChange={handleChange} />

      <select name="country" required className="block w-full p-2 border rounded" onChange={handleChange}>
        <option value="">Select Country</option>
        <option value="United States">United States</option>
        <option value="Germany">Germany</option>
        <option value="France">France</option>
        <option value="UK">United Kingdom</option>
        <option value="Other">Other</option>
      </select>

      <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded">
        Create Account
      </button>
    </form>
  );
}

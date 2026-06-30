import React from 'react'
import Header from '../components/Header'
import SpecialityMenu from '../components/SpecialityMenu'
import TopDoctors from '../components/TopDoctors'
import Banner from '../components/Banner'
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <Header />
      <SpecialityMenu />
      <TopDoctors />

      <div className="my-12 text-center">
        <h2 className="text-2xl font-semibold mb-6">
          Health Risk Prediction
        </h2>

        <div className="flex justify-center gap-6 flex-wrap">
          
          <Link to="/predict/diabetes">
            <button className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600">
              Diabetes Prediction
            </button>
          </Link>

          <Link to="/predict/heart">
            <button className="bg-red-500 text-white px-6 py-3 rounded-lg hover:bg-red-600">
              Heart Disease Prediction
            </button>
          </Link>

        </div>
      </div>

      <Banner />
    </div>
  )
}

export default Home
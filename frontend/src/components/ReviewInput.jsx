import { useState } from "react";

import api from "../api/api";

import Loader from "./Loader";

import PredictionCard from "./PredictionCard";


function ReviewInput() {

    const [review, setReview] = useState("");

    const [loading, setLoading] = useState(false);

    const [prediction, setPrediction] = useState("");

    const [confidence, setConfidence] = useState(0);


    const analyzeReview = async () => {

        if (review.trim() === "") {

            alert("Please enter a review.");

            return;
        }

        try {

            setLoading(true);

            const response = await api.post("/predict", {

                review: review,

            });

            setPrediction(response.data.prediction);

            setConfidence(response.data.confidence);

        }

        catch (err) {

            console.log(err);

            alert("Something went wrong.");

        }

        finally {

            setLoading(false);

        }

    };


    return (
        <div className="" style={{  borderRadius: "0.5rem" ,marginTop:"-240px"}}>
            <textarea
                rows={7}
                className="w-full bg-transparent border border-slate-700 rounded-lg p-4 text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#00b4ff]/30"
                placeholder="Enter movie review..."
                value={review}
                onChange={(e) => setReview(e.target.value)}
            />

            <div className="flex items-center gap-4 mt-5">
                <button
                    onClick={analyzeReview}
                    className="px-6 py-3 rounded-lg bg-gradient-to-r from-[#00b4ff] to-[#0066ff] text-black font-semibold shadow-sm hover:opacity-95"
                >
                    Analyze Review
                </button>
                <div className="flex-1">
                    {loading && <Loader />}
                </div>
            </div>

            <div className="mt-6">
                <PredictionCard prediction={prediction} confidence={confidence} />
            </div>
        </div>
    );

}

export default ReviewInput;
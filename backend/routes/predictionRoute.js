import express from "express";
import authUser from "../middleware/authUser.js";
import { predictDiabetes, predictHeart } from "../controllers/predictionController.js";

const predictionRouter = express.Router();

predictionRouter.post("/diabetes", authUser, predictDiabetes);
predictionRouter.post("/heart", authUser, predictHeart);

export default predictionRouter;

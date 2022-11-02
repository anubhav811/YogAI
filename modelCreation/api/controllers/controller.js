const asyncHandler = require("express-async-handler");

// @desc get all Poses
// @route GET api/Poses
// @access Private
const getPoses = asyncHandler(async (req, res) => {
  res.send({
    message: "Get Poses",
  });
});

// @desc set yoga
// @route POST api/Poses
// @access Private
const setPoses = asyncHandler(async (req, res) => {
  if (!req.body.text) {
    res.status(400);
    throw new Error("Please add a text field");
  }
  console.log(req.body);

});
// @desc update yoga with id
// @route PUT api/Poses/:id
// @access Private
const updateyoga = asynchHandler(async (req, res) => {
  res.send({
    message: `Update yoga for id=${req.params.id}`,
  });
});

// @desc delete yoga with id
// @route PUT api/Poses/:id
// @access Private
const deleteyoga = asyncHandler(async (req, res) => {
  res.send({
    message: `Delete yoga for id=${req.params.id}`,
  });
});
module.exports = { getPoses, setPoses, updateyoga, deleteyoga };

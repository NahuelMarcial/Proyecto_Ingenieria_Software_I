import { Card, CardActionArea, CardMedia, Typography } from "@mui/material";

const FigureCard = ({ imageSrc, title }) => {
  return (
    <Card sx={{ maxWidth: 140, padding: "1px", borderRadius: "20px" }}>
      <CardActionArea>
        <CardMedia component="img" height="140" image={imageSrc} alt={title} />
        <Typography variant="h4" align="center">
          {title}
        </Typography>
      </CardActionArea>
    </Card>
  );
};

export default FigureCard;

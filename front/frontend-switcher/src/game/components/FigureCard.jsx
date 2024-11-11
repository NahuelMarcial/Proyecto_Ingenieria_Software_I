import { Card, CardActionArea, CardMedia, Box } from "@mui/material";
import { motion } from "framer-motion";
import BlockCardIcon from "../../assets/icons/BlockCardIcon";

const FigureCard = ({
  imageSrc,
  title,
  isClicked,
  isBlocked,
  isForBlock,
  onClick,
}) => {
  return (
    <Box position="relative" display="inline-block">
      <motion.div
        animate={{
          scale: isClicked ? 1.05 : 1, // Escala al 110% cuando está seleccionada
        }}
        transition={{ type: "spring", stiffness: 300, damping: 20 }} // Transición suave
      >
        <Card
          sx={{
            maxWidth: 110,
            padding: "2px",
            borderRadius: "5px",
            border: isClicked
              ? isForBlock
                ? "4px solid"
                : "4px solid"
              : "2px solid",
            borderColor: isClicked
              ? isForBlock
                ? "error.dark"
                : "primary.dark"
              : "grey.700",
            boxShadow: isClicked ? "5px 5px 2px rgba(0, 0, 0, 0.4)" : "none",
          }}
        >
          <CardActionArea onClick={onClick} disabled={isBlocked}>
            <CardMedia
              component="img"
              height="110"
              image={imageSrc}
              alt={title}
            />
          </CardActionArea>
        </Card>
      </motion.div>
      {isBlocked && (
        <Box
          position="absolute"
          top={0}
          left={0}
          width="100%"
          height="100%"
          sx={{ backgroundColor: "rgba(0, 0, 0, 0.5)" }}
        >
          <BlockCardIcon size={46.5} />
        </Box>
      )}
    </Box>
  );
};

export default FigureCard;

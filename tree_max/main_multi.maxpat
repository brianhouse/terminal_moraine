{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 1,
			"revision" : 10,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 431.0, -813.0, 754.0, 812.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 142.0, 195.0, 51.0, 22.0 ],
					"text" : "phrases"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 159.25, 665.0, 83.0, 22.0 ],
					"text" : "loadmess 100"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "gain~",
					"multichannelvariant" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 64.25, 632.0, 22.0, 49.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "gain~",
					"multichannelvariant" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 44.25, 632.0, 22.0, 49.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 16,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "signal" ],
					"patching_rect" : [ 40.75, 585.0, 682.0, 22.0 ],
					"saved_object_attributes" : 					{
						"active" : [ 1, 1 ],
						"aed_scale" : 10.0,
						"coord_angles" : 0,
						"coord_system" : 0,
						"gain" : 1.0,
						"order" : 3,
						"orderweight" : [ 1.0, 0.6, 0.2, 0.028571428571429 ],
						"type" : 1,
						"xyz_scale" : 10.0
					}
,
					"text" : "ambidecode~ 3 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 64,
					"outlettype" : [ "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal" ],
					"patching_rect" : [ 42.25, 520.0, 680.5, 22.0 ],
					"text" : "mc.unpack~ 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-35",
					"maxclass" : "newobj",
					"numinlets" : 64,
					"numoutlets" : 16,
					"outlettype" : [ "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal" ],
					"patching_rect" : [ 42.25, 553.0, 680.5, 22.0 ],
					"saved_object_attributes" : 					{
						"active" : [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
						"aed_scale" : 10.0,
						"center_att_db" : 6.0,
						"center_curve" : 0.2,
						"center_size" : 1.0,
						"coord_angles" : 0,
						"coord_system" : 0,
						"db_unit" : 1.5,
						"dist_att" : 1.0,
						"distance_mode" : 1,
						"gain" : 1.0,
						"interpolation" : 1,
						"order" : 3,
						"type" : 1,
						"xyz_scale" : 10.0
					}
,
					"text" : "ambiencode~ 3 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 44.25, 683.0, 45.0, 45.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "meter~",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 121.25, 632.0, 12.0, 58.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-42",
					"maxclass" : "meter~",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 103.25, 632.0, 12.0, 58.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 531.0, 104.5, 150.0, 20.0 ],
					"text" : "30s per year for 10 years"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 485.0, 78.0, 150.0, 20.0 ],
					"text" : "start tree generation"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 531.0, 139.0, 38.0, 22.0 ],
					"text" : "/stop/"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-29",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 454.0, 104.5, 72.0, 22.0 ],
					"text" : "/start/ 30 10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 454.0, 172.0, 138.0, 22.0 ],
					"text" : "udpsend 127.0.0.1 6006"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 1,
							"revision" : 10,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 212.0, 150.0, 213.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"comment" : "mc.audio for ambi endocing in ST",
									"id" : "obj-2",
									"ignoreclick" : 1,
									"index" : 2,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "multichannelsignal" ],
									"patching_rect" : [ 132.0, 139.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "control data for ST",
									"id" : "obj-1",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 51.0, 139.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-24",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 51.0, 382.0, 138.0, 22.0 ],
									"text" : "udpsend 127.0.0.1 5005"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-22",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 132.0, 280.0, 54.0, 22.0 ],
									"text" : "mc.dac~"
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-24", 0 ],
									"source" : [ "obj-1", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-22", 0 ],
									"source" : [ "obj-2", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 112.0, 447.0, 60.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p to_ST"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 189.0, 406.0, 56.0, 20.0 ],
					"text" : "output:",
					"textcolor" : [ 0.031372549019608, 0.654901960784314, 0.847058823529412, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.674509803921569, 0.898039215686275, 0.980392156862745, 1.0 ],
					"bgcolor2" : [ 0.674509803921569, 0.898039215686275, 0.980392156862745, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.556862745098039, 0.737254901960784, 1.0, 1.0 ],
					"bgfillcolor_color1" : [ 0.674509803921569, 0.898039215686275, 0.980392156862745, 1.0 ],
					"bgfillcolor_color2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_proportion" : 0.5,
					"bgfillcolor_type" : "color",
					"gradient" : 1,
					"id" : "obj-37",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 234.0, 405.0, 63.0, 22.0 ],
					"text" : "ICST"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 168.0, 357.5, 29.5, 22.0 ],
					"text" : "ST"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 128.5, 357.5, 36.0, 22.0 ],
					"text" : "ICST"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 5,
					"outlettype" : [ "", "multichannelsignal", "", "multichannelsignal", "" ],
					"patching_rect" : [ 81.0, 405.0, 81.0, 22.0 ],
					"text" : "ambidextrous"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-53",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 159.25, 706.0, 58.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-52",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 181.25, 763.0, 90.0, 22.0 ],
					"text" : "xyz 2 0.75 0. 0."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-51",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 159.25, 736.0, 94.0, 22.0 ],
					"text" : "xyz 1 -0.75 0. 0."
				}

			}
, 			{
				"box" : 				{
					"border_color" : [ 0.32549, 0.32549, 0.32549, 1.0 ],
					"circle_color" : [ 0.0, 0.0, 0.0, 0.05098 ],
					"coord_color" : [ 0.584314, 0.584314, 0.584314, 1.0 ],
					"grid" : 1,
					"grid_color" : [ 0.0, 0.0, 0.0, 0.05098 ],
					"gridunit_ae" : 8,
					"hi_border_color" : [ 0.776471, 0.635294, 0.776471, 1.0 ],
					"hi_grid_color" : [ 0.0, 0.0, 0.0, 0.101961 ],
					"id" : "obj-114",
					"line_color" : [ 1.0, 0.47451, 0.0, 1.0 ],
					"maxclass" : "ambimonitor",
					"name_color" : [ 0.360784, 0.341176, 0.321569, 1.0 ],
					"number_font_size" : 9.0,
					"numbers" : 1,
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 281.0, 632.0, 101.0, 101.0 ],
					"point_color" : [ 0.360784, 0.341176, 0.321569, 1.0 ],
					"point_color1" : [ 0.74902, 0.0, 0.0, 1.0 ],
					"point_color2" : [ 0.0, 0.74902, 0.0, 1.0 ],
					"point_color3" : [ 0.701961, 0.0, 1.0, 1.0 ],
					"point_color4" : [ 0.74902, 0.380392, 0.0, 1.0 ],
					"point_size" : 5.0,
					"prototypename" : "small_light_grey"
				}

			}
, 			{
				"box" : 				{
					"circle_color" : [ 0.925490196078431, 0.92156862745098, 0.92156862745098, 1.0 ],
					"grid" : 2,
					"grid_color" : [ 0.890196078431372, 0.890196078431372, 0.890196078431372, 1.0 ],
					"hi_grid_color" : [ 0.831372549019608, 0.831372549019608, 0.831372549019608, 1.0 ],
					"id" : "obj-18",
					"maxclass" : "ambimonitor",
					"numinlets" : 1,
					"numoutlets" : 3,
					"offset" : 1,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 285.0, 219.0, 136.0, 136.0 ],
					"point_size" : 4.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 285.0, 186.0, 93.0, 22.0 ],
					"text" : "xyz $1 $5 $6 $7"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "meter~",
					"numinlets" : 1,
					"numoutlets" : 1,
					"orientation" : 2,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 81.0, 226.0, 198.0, 114.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-17",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 30.0, 148.0, 109.0, 22.0 ],
					"text" : "target $1, $2 $3 $4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 30.0, 195.0, 99.0, 22.0 ],
					"text" : "mc.poly~ limb 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 103.0, 83.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 30.0, 83.0, 65.0, 22.0 ],
					"text" : "route limb/"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 30.0, 45.0, 97.0, 22.0 ],
					"text" : "udpreceive 5005"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 0 ],
					"order" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"order" : 1,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-114", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 1 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-16", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 1 ],
					"midpoints" : [ 152.5, 437.0, 181.0, 437.0, 181.0, 394.0, 287.5, 394.0 ],
					"source" : [ "obj-16", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 1 ],
					"source" : [ "obj-16", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 0 ],
					"source" : [ "obj-16", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-26", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"order" : 0,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"order" : 1,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"order" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"order" : 1,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"order" : 1,
					"source" : [ "obj-30", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"order" : 1,
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"order" : 0,
					"source" : [ "obj-30", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"order" : 0,
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 2 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 63 ],
					"source" : [ "obj-33", 63 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 62 ],
					"source" : [ "obj-33", 62 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 61 ],
					"source" : [ "obj-33", 61 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 60 ],
					"source" : [ "obj-33", 60 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 59 ],
					"source" : [ "obj-33", 59 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 58 ],
					"source" : [ "obj-33", 58 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 57 ],
					"source" : [ "obj-33", 57 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 56 ],
					"source" : [ "obj-33", 56 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 55 ],
					"source" : [ "obj-33", 55 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 54 ],
					"source" : [ "obj-33", 54 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 53 ],
					"source" : [ "obj-33", 53 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 52 ],
					"source" : [ "obj-33", 52 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 51 ],
					"source" : [ "obj-33", 51 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 50 ],
					"source" : [ "obj-33", 50 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 49 ],
					"source" : [ "obj-33", 49 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 48 ],
					"source" : [ "obj-33", 48 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 47 ],
					"source" : [ "obj-33", 47 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 46 ],
					"source" : [ "obj-33", 46 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 45 ],
					"source" : [ "obj-33", 45 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 44 ],
					"source" : [ "obj-33", 44 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 43 ],
					"source" : [ "obj-33", 43 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 42 ],
					"source" : [ "obj-33", 42 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 41 ],
					"source" : [ "obj-33", 41 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 40 ],
					"source" : [ "obj-33", 40 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 39 ],
					"source" : [ "obj-33", 39 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 38 ],
					"source" : [ "obj-33", 38 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 37 ],
					"source" : [ "obj-33", 37 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 36 ],
					"source" : [ "obj-33", 36 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 35 ],
					"source" : [ "obj-33", 35 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 34 ],
					"source" : [ "obj-33", 34 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 33 ],
					"source" : [ "obj-33", 33 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 32 ],
					"source" : [ "obj-33", 32 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 31 ],
					"source" : [ "obj-33", 31 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 30 ],
					"source" : [ "obj-33", 30 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 29 ],
					"source" : [ "obj-33", 29 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 28 ],
					"source" : [ "obj-33", 28 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 27 ],
					"source" : [ "obj-33", 27 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 26 ],
					"source" : [ "obj-33", 26 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 25 ],
					"source" : [ "obj-33", 25 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 24 ],
					"source" : [ "obj-33", 24 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 23 ],
					"source" : [ "obj-33", 23 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 22 ],
					"source" : [ "obj-33", 22 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 21 ],
					"source" : [ "obj-33", 21 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 20 ],
					"source" : [ "obj-33", 20 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 19 ],
					"source" : [ "obj-33", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 18 ],
					"source" : [ "obj-33", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 17 ],
					"source" : [ "obj-33", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 16 ],
					"source" : [ "obj-33", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 15 ],
					"source" : [ "obj-33", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 14 ],
					"source" : [ "obj-33", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 13 ],
					"source" : [ "obj-33", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 12 ],
					"source" : [ "obj-33", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 11 ],
					"source" : [ "obj-33", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 10 ],
					"source" : [ "obj-33", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 9 ],
					"source" : [ "obj-33", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 8 ],
					"source" : [ "obj-33", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 7 ],
					"source" : [ "obj-33", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 6 ],
					"source" : [ "obj-33", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 5 ],
					"source" : [ "obj-33", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 4 ],
					"source" : [ "obj-33", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 3 ],
					"source" : [ "obj-33", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 2 ],
					"source" : [ "obj-33", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 1 ],
					"source" : [ "obj-33", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 15 ],
					"source" : [ "obj-35", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 14 ],
					"source" : [ "obj-35", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 13 ],
					"source" : [ "obj-35", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 12 ],
					"source" : [ "obj-35", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 11 ],
					"source" : [ "obj-35", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 10 ],
					"source" : [ "obj-35", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 9 ],
					"source" : [ "obj-35", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 8 ],
					"source" : [ "obj-35", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 7 ],
					"source" : [ "obj-35", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 6 ],
					"source" : [ "obj-35", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 5 ],
					"source" : [ "obj-35", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 4 ],
					"source" : [ "obj-35", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 3 ],
					"source" : [ "obj-35", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 2 ],
					"source" : [ "obj-35", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 1 ],
					"source" : [ "obj-35", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 2 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-114", 0 ],
					"source" : [ "obj-51", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-114", 0 ],
					"source" : [ "obj-52", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"order" : 1,
					"source" : [ "obj-53", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-52", 0 ],
					"order" : 0,
					"source" : [ "obj-53", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 1 ],
					"order" : 0,
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"order" : 1,
					"source" : [ "obj-8", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "limb.maxpat",
				"bootpath" : "~/Studio/terminal_morraine/code/tree_max",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "ambidextrous.maxpat",
				"bootpath" : "~/Studio/terminal_morraine/code/tree_max",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "phrases.maxpat",
				"bootpath" : "~/Studio/terminal_morraine/code/tree_max",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "ambimonitor.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "ambiencode~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "ambidecode~.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0
	}

}
